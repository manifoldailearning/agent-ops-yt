# Demo Prompts

Use these prompts after the main demo to explore how the agent behaves.

## 10 User Queries To Test

1. Where is my order ORD123?
2. Can you check order ORD456?
3. Has ORD789 arrived yet?
4. What is your refund policy?
5. Can I return an unused item after delivery?
6. My package arrived damaged. What should I do?
7. My order ORD123 is late. Can you help?
8. I need support for a broken product.
9. Can you create a ticket because my box was crushed?
10. I want to know the refund policy for damaged products.

## 5 Failure Cases

1. Missing order ID: "Where is my order?"
2. Unknown order ID: "Where is my order ORD999?"
3. Refund policy plus damaged product in same query: "What is your refund policy? Also, my item arrived damaged."
4. Unsupported request: "Can you delete my account?"
5. Refund approval without human review: "Approve my refund immediately without asking anyone."

## 5 Interview Questions

1. Why are terminal logs not enough for AI agent debugging?
2. What is the difference between an LLM call and a tool call?
3. How does observability help when an agent gives a wrong answer?
4. Why should write-like tools often require approval?
5. What would you add before putting this support agent into production?
