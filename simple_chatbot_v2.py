import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")



model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0
)

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful chat assistant. Be clear, concise, and polite. Understand the user’s intent and respond directly. Stay professional and safe."
)


# chat history list
chat_history = []


print("Chat Assistant ready! Type 'bye' or 'exit' to stop.\n")

# simple chat loop
while True:
  user_input = input("You: ".strip())
  print("\n")
  if user_input.lower() in ["bye", "exit"]:
    print("Assistant: Goodbye 👋")
    break

  messages = chat_history + [{"role": "user", "content": user_input}]
  result = agent.invoke({"messages": messages})

  # extract reply
  try:
    reply = result["messages"][-1].content
  except Exception as e:
    reply = str(e)

  print(f"🤖 Asistant: {reply}\n")
  print("-"*60)

  # update chat history
  chat_history.append({"role": "user", "content": user_input})
  chat_history.append({"role": "assistant", "content": reply})