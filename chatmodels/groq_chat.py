from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file



from langchain_groq import ChatGroq

model= ChatGroq(
    model="openai/gpt-oss-120b",
)


response = model.invoke("What is the capital of Bihar?")

print(response.content)