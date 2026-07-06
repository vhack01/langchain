from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1000)
result = embedding.embed_query("Hi, my name is Vishwas Kumar.")

print(result)