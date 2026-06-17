# AgentOps Tutorial: Trace Your First AI Agent

This beginner-friendly project builds a tiny customer support AI agent and traces its work with AgentOps.


## 1. What This Project Shows

- How to create a simple agent with the OpenAI Agents SDK
- How to add small Python tools to an agent
- How to initialize AgentOps tracing
- How to run demo customer support questions
- How to inspect agent behavior beyond terminal logs

## 2. Why Agent Observability Matters

Terminal logs usually show only what your script printed. Agent observability helps you inspect what happened inside the agent run:

- Which LLM calls were made
- Which tools were selected
- What each tool returned
- How long steps took
- Where failures occurred
- How the final answer was produced

This matters because agent behavior can be non-obvious. A good trace helps you debug, explain, and improve the system.

## 3. Architecture Flow

```text
User Query -> Agent -> Tool Call -> Tool Result -> Final Response -> AgentOps Trace
```

The mini support agent can:

- Look up hardcoded order status
- Explain the refund policy
- Suggest a mock support ticket for damaged product cases

## 4. Setup Instructions

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Add your keys to `.env`:

```text
OPENAI_API_KEY=your_openai_api_key_here
AGENTOPS_API_KEY=your_agentops_api_key_here
```

Run the demo:

```bash
python main.py
```

## 5. Demo Queries

The script runs these three queries:

```text
Where is my order ORD123?
What is your refund policy?
My product arrived damaged. Can you create a ticket?
```

For each query, the terminal prints:

- A clean divider
- The user query
- The final response
- A reminder to check the AgentOps dashboard

## 6. What To Check In AgentOps Dashboard

After running the script, open AgentOps and look for:

- Session
- Model call
- Tool call
- Tool result
- Final response
- Latency
- Errors, if any

The important lesson: the dashboard shows the agent's internal steps, not just the final answer.

## 7. What This Demo Does Not Cover

- Production authentication
- Real ticketing API
- Database
- RAG
- Deployment
- Evals
- Human approval workflow

## 8. Production Improvements

For a real support agent, you would likely add:

- Approval for write tools
- Application logging
- Trace IDs in logs and responses
- Evals for response quality
- Cost tracking
- Latency monitoring
- Tool permissioning
- Fallback handling
- PII masking
- Audit logs

## 9. Resume Bullet

Built a simple AI support agent using OpenAI Agents SDK and AgentOps to trace user queries, tool calls, and final responses for basic agent observability.

## 10. Interview Explanation

This project demonstrates why agent observability matters. Instead of only seeing the final answer, we can inspect what the agent did internally - which tool it selected, what the tool returned, and how the final response was generated.

In an interview, you can explain:

- The agent receives a user query.
- The LLM decides whether a tool is needed.
- The tool returns structured information from the app side.
- The LLM uses that tool result to produce the final answer.
- AgentOps gives a trace so engineers can debug and review the run.

## 11. Next Steps

- Try the extra prompts in `demo_prompts.md`
- Add another hardcoded order
- Add a human approval step before ticket creation
- Compare terminal output with the AgentOps trace
- Add eval cases for common support questions
