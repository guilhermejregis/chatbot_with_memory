import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="PDF Reader", layout="centered")
st.title("PDF Reader")

st.header("Leitor de PDF")
arquivos = st.file_uploader("Carregar arquivo PDF", type="pdf")

if arquivos:
    st.success(f"Arquivo carregado: {arquivos.name}")

    pdf_reader = PdfReader(arquivos)
    st.subheader("Conteúdo do PDF:")
    st.write(f"Número de páginas: {len(pdf_reader.pages)}")
    
    for num, page in enumerate(pdf_reader.pages):
        texto = page.extract_text()
        if texto:
            with st.expander(f"Página {num + 1}"):
                st.text(texto)
        else:
            st.warning(f"Página {num +1} não contém nenhum texto legível.")

