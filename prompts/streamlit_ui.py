from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
load_dotenv()

model = ChatOpenAI(model="gpt-4")

st.header("Research Tool")

col1, col2, col3 = st.columns(3)

with col1:
    paper_input = st.selectbox(
        "Select Research Paper",
        ("Attenttion All you need" "Language Models are Few-Shot Learners", "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)", "Mastering the game of Go with deep neural networks and tree search (AlphaGo) (2016)") 
    )

with col2: 
    explanation_style =st.selectbox("Select explantion style", 
    ("Beginner-Friendly", "Technical", "Code-oriented", "Mathematical"))

with col3:
    explanation_length = st.selectbox("Select expaination length", 
    ("Long-form" , "Short-form", "Key points"))

template = load_prompt("./json_prompts/prompt_template.json")

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'explanation_style': explanation_style,
#     'explanation_length': explanation_length
# })

if st.button("Summarize"):
    # chain
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'explanation_style': explanation_style,
        'explanation_length': explanation_length
    })

    # result = model.invoke(prompt)
    st.write(result.content)
