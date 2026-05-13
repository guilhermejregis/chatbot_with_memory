import streamlit as st
from langchain_ollama import ChatOllama

# Configuração da página
st.set_page_config(
    page_title="AI Multi-Model Assistant",
    layout="centered"
)

st.title("🤖 CHATBOT LOCAL")

st.sidebar.success("Menu")

# Modelos disponíveis
MODELOS = {

    "DEEPSEEK": {
        "model": "deepseek-r1:1.5b",
        "description": "Programação e raciocínio"
    },

    "LLAMA 3": {
        "model": "llama3",
        "description": "Uso geral"
    },

    "GEMMA 2B": {
        "model": "gemma:2b",
        "description": "Modelo leve e rápido"
    },

    "MISTRAL": {
        "model": "mistral",
        "description": "Geral e rápido"
    }
}

# Escolha do modelo
modelo_escolhido = st.sidebar.selectbox(
    "Escolha seu modelo",
    list(MODELOS.keys())
)

# Informações do modelo
info = MODELOS[modelo_escolhido]

st.sidebar.info(info["description"])

# Modelo atual
st.caption(f"Modelo atual: {modelo_escolhido}")

# Inicialização do modelo
llm = ChatOllama(
    model=info["model"],
    base_url="http://localhost:11435"
)

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state["messages"]

# Exibe mensagens anteriores
for role, content in messages:

    with st.chat_message(role):
        st.markdown(content)

# Input do usuário
in_message = st.chat_input(
    "Digite sua mensagem aqui..."
)

if in_message:

    # Salva mensagem do usuário
    messages.append(("user", in_message))

    with st.chat_message("user"):
        st.markdown(in_message)

    try:

        # Loader
        with st.spinner("Pensando..."):

            response = llm.invoke(in_message).content

        # Salva resposta
        messages.append(("assistant", response))

        # Mostra resposta
        with st.chat_message("assistant"):
            st.markdown(response)

    except Exception as e:

        st.error(
            f"Erro ao conectar com Ollama: {e}"
        )

# Botão limpar conversa
if st.sidebar.button("🗑️ Limpar conversa"):

    st.session_state.messages = []

    st.rerun()