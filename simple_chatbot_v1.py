
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0
)

agent = create_agent(
    model=model,
    tools=[],
    system_prompt=(
        "You are a helpful chat assistant. "
        "Be clear, concise, and polite. "
        "Understand the user's intent and respond directly. "
        "Stay professional and safe."
    )
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Explain Machine Learning in short"
            }
        ]
    }
)

print(result["messages"][-1].content)
