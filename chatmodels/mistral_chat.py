from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model = "mistral-small-2603",
    temperature = 0.5,
    max_tokens = 1000 
)

response = model.invoke("What is machine Learning?")

print(response.content)