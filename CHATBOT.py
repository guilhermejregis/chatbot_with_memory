import streamlit as st
from langchain_ollama import ChatOllama

MODELOS = {


    "DEEPSEEK": {
        "model": "deepseek-r1:1.5b",
        "description": "Programação e raciocínio"
    },
    
    "LLAMA 3": {
        "model": "llama-3",
        "description": "Geral"
    },

    "GEMMA 2B":{
        "model": "gemma-2b",
        "description": "Rapidez"
    },
    
    "Mistral":{
        "model": "mistral",
        "description": "Geral e rápido"
    }
}

modelo_escolhido = st.selectbox("Escolha seu modelo",
                                list(MODELOS.keys()))


info = MODELOS[modelo_escolhido]

st.sidebar.info(info["description"])



llm = ChatOllama(
    model=info["model"],
    base_url="http://localhost:11434"
                 )

st.set_page_config(page_title="Deepseek R1:1.5B", layout="centered")
st.title("CHATBOT")


st.sidebar.success("Menu")

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
    chat.markdown(response)