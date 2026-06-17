"""Simple tools for the Mini Customer Support Agent demo."""

from agents import function_tool


ORDER_STATUSES = {
    "ORD123": "shipped, expected delivery tomorrow",
    "ORD456": "processing, expected dispatch in 2 days",
    "ORD789": "delivered yesterday",
}


@function_tool
def get_order_status(order_id: str) -> str:
    """Look up a hardcoded order status by order ID."""
    normalized_order_id = order_id.strip().upper()
    status = ORDER_STATUSES.get(normalized_order_id)

    if status is None:
        return (
            f"No order status was found for {normalized_order_id}. "
            "Ask the customer to verify the order ID."
        )

    return f"Order {normalized_order_id} is {status}."


@function_tool
def get_refund_policy() -> str:
    """Return the store refund policy."""
    return (
        "Refunds are allowed within 7 days of delivery. "
        "The product must be unused and in original packaging. "
        "Damaged product cases should be escalated to support."
    )


@function_tool
def create_support_ticket(issue: str) -> str:
    """Return a mock support ticket ID for the reported issue."""
    # In real systems, write tools should often require approval before they
    # change customer data, create tickets, issue refunds, or send messages.
    return f"Mock support ticket created: TICKET-1001. Issue: {issue}"
