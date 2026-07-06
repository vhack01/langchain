from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs={"temperature":0.5, "max_new_tokens":200}
)
    
model = ChatHuggingFace(llm=llm)

res = model.invoke("Tell me a poem on cricket.")
print(res.content)