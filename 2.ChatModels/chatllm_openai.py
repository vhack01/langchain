from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.5, max_completion_tokens=10)

result = model.invoke("""Create a resume of a software engineer who had 2 years of experience. His skills are:
- Java
- Spring Boot
- AWS
- AI Agent 
- Docker
- K6
- Spring Framework
Create create a three-line summary of the resume.""");
print(result.content)