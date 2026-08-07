from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.6,
    max_tokens=1000
)
print("Type 1 for Funny Ai")
print("Type 2 for Professional Ai")
print("Type 3 for Friendly Ai")
print("Type 4 for Sarcastic Ai")
choice = input("Type your choice:")
if choice == "1":
    choice = "Funny"
elif choice == "2":
    choice = "Professional"
elif choice == "3":
    choice = "Friendly"
elif choice == "4":
    choice = "Sarcastic"
else:
    print("Invalid choice. Please try again.")
    exit()
chat_history = [
    SystemMessage(content=f"You are a {choice} assistant."),
]

print("--------Welcome to the AI Chatbot! Type 'exit' to quit.--------")
while True:
    query = HumanMessage(content=input("You:"))
    if query.content == "exit":
        break
    chat_history.append(query)
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)
print("CHAT HISTORY:", chat_history)
print("--------Thank you for using the AI Chatbot! Goodbye!--------")