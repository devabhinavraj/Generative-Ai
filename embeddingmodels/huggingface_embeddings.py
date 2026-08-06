from dotenv import load_dotenv


load_dotenv() 

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts = [
    "Hello, how are you?",
    "I am fine, thank you!",
    "I Love programming in Python.",
    "I enjoy learning about AI and machine learning.",
]

vectors = embeddings.embed_documents(texts)

print(str(vectors))