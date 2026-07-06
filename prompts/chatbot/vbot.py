from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()

model = ChatOpenAI(model="gpt-4o")


# UI of chatbot
st.title("VHACK 👨 BOT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(name=message["role"]):
        st.write(message["content"])


prompt = st.chat_input("Type here...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message(name="User"):
        st.write(prompt)

    result = model.invoke(st.session_state.messages)
    st.session_state.messages.append({"role" :"assistant", "content" :result.content})

    with st.chat_message(name="Assistant"):
        st.write(result.content)
