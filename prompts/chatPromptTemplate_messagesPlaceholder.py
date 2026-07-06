from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# create template 
template = ChatPromptTemplate([
    ("system", "You are a helpful AI assistant"), 
    MessagesPlaceholder(variable_name = "chat_history"),
    ("user", "{query}")
])

# load chat history
chat_history = []
with open("./chat_history.txt") as f:
    chat_history.extend(f.readlines())


# create prompt
prompt = template.invoke({"chat_history": chat_history, "query": "what is the status of my refund"})
print(prompt)