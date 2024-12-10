from langchain_ollama import OllamaLLM
import streamlit as st

llm = OllamaLLM(model="llama3")
st.title("Chatbot using Llama3 by Gustavo Casado")

prompt = st.text_area("Ingresa tu pregunta")

if st.button("Generar respuesta"):
    if prompt:
        with st.spinner("Generando..."):
            st.write_stream(llm.stream(prompt))
