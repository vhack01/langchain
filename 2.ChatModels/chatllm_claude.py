from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-haiku-4-5-20251001')
result = model.invoke("Hello, how are you?")
print(result.content)