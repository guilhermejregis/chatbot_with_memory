import streamlit as st
from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b",
                 url="http://localhost:11434")

st.set_page_config(page_title="Deepseek R1:1.5B", layout="centered")
st.title("TESTE COM DEEPSEEK")

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state["messages"]
for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)

in_message = st.chat_input("Digite sua mensagem aqui...")
if in_message:
    messages.append(("human", in_message))
    chat = st.chat_message("human")
    chat.markdown(in_message)
    response = llm.invoke(messages).content
    messages.append(("ai", response))
    chat = st.chat_message("ai")
    chat.markdown(response.content)