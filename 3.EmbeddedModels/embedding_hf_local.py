from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India."
print(model.encode(text))