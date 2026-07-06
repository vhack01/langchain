from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

documents = [
    "Kolkata is a major city in the state of West Bengal.",
    "Paris is the capital of France.",
    "My name is Vishwas kumar"
]

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=10)
result = embedding.embed_documents(documents)

print(result)