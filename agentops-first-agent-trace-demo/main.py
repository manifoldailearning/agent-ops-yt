"""Run a tiny OpenAI Agents SDK workflow and trace it with AgentOps."""

import os
import sys

from agents import Agent, Runner
from dotenv import load_dotenv
from tools import create_support_ticket, get_order_status, get_refund_policy


DEMO_QUERIES = [
    "Where is my order ORD123?",
    "What is your refund policy?",
    "My product arrived damaged. Can you create a ticket?",
]


SUPPORT_AGENT_INSTRUCTIONS = """
You are a helpful customer support AI assistant.
Use tools when needed.
If the user asks about order status, call get_order_status.
If the user asks about refund policy, call get_refund_policy.
If the user wants escalation or reports a damaged product, use create_support_ticket.
Keep answers short and clear.
Never invent order status.
If order ID is missing, ask the user for the order ID.
For write-like actions such as ticket creation, explain that real production systems may require human approval.
"""


def check_required_environment() -> None:
    """Show a friendly setup message if required API keys are missing."""
    missing_keys = [
        key
        for key in ("OPENAI_API_KEY", "AGENTOPS_API_KEY")
        if not os.getenv(key)
    ]

    if not missing_keys:
        return

    print("Missing required environment variables:")
    for key in missing_keys:
        print(f"- {key}")
    print()
    print("Create a .env file from .env.example and add your API keys:")
    print("cp .env.example .env")
    sys.exit(1)


def initialize_agentops() -> None:
    """Start AgentOps tracing before the agent runs."""
    import agentops
    from agentops.instrumentation.agentic.openai_agents import OpenAIAgentsInstrumentor

    # AgentOps captures the session trace so you can inspect what happened
    # after the script finishes. The dashboard helps you review LLM calls,
    # tool calls, latency, failures, and the final response.
    agentops.init(instrument_llm_calls=False)
    OpenAIAgentsInstrumentor().instrument()


def build_agent() -> Agent:
    """Create the support agent after AgentOps has been initialized."""
    return Agent(
        name="SupportAgent",
        instructions=SUPPORT_AGENT_INSTRUCTIONS,
        tools=[
            get_order_status,
            get_refund_policy,
            create_support_ticket,
        ],
    )


def run_demo_query(agent: Agent, query: str) -> None:
    """Run one query and print the final answer."""
    print("\n" + "=" * 72)
    print(f"User query: {query}")
    print("-" * 72)

    result = Runner.run_sync(agent, query)

    print("Final response:")
    print(result.final_output)
    print()
    print("Trace note: check the AgentOps dashboard for the session trace.")


def main() -> None:
    load_dotenv()
    check_required_environment()
    initialize_agentops()

    agent = build_agent()

    for query in DEMO_QUERIES:
        run_demo_query(agent, query)

    print("\nDemo complete. Open AgentOps to inspect the LLM and tool traces.")


if __name__ == "__main__":
    main()
