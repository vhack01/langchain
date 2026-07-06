from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

document = [
    "Virat Kohli is a world class cricketer.",
    "Virat Kohli is a right handed batsman.",
    "Virat Kohli scored 121 runs in the match.",
    "Kohli is a legend of the game.",
    "Rohit Sharma is also a great batsman.",
    "Rohit Sharma scored 200 runs in the match.",
    "Rohit Sharma is a right handed batsman.",
    "Rohit Sharma is a legend of the game.",
]


embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=100)
doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query("score of virat kohli?")

similarity_score= cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(similarity_score)), key= lambda x: x[1], reverse=True)[0]

print("Query : ", "score of virat kohli?")
print("Result: ", document[index])
print("Score: ", score)