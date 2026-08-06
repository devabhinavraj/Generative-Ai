from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file



from langchain_groq import ChatGroq

model= ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.9,
    max_tokens=300 
)


response = model.invoke("Write a short poem about AI.")

print(response.content)