import streamlit as st
from chatbot_utils import obtener_respuesta_ia, procesar_archivo_contexto

st.set_page_config(page_title="AI Chatbot con Contexto", page_icon="🤖")
st.title("🤖 Mi Chatbot de IA Personalizado")
st.write("Sube un archivo de texto para darle contexto al bot o chatea directamente con él.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un asistente de IA muy útil, preciso y educado."}
    ]

with st.sidebar:
    st.header("📁 Datos de Contexto")
    archivo = st.file_uploader("Sube un archivo .txt para entrenar temporalmente al bot", type=["txt"])
    
    if archivo:
        contexto = procesar_archivo_contexto(archivo)
        st.success("¡Archivo cargado con éxito!")
        st.session_state.messages[0]["content"] = f"Eres un asistente de IA. Usa el siguiente contexto para responder las preguntas del usuario si es relevante:\n\n{contexto}"

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

if prompt := st.chat_input("¿En qué te puedo ayudar hoy?"):
    with st.chat_message("user"):
        st.write(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            respuesta_bot = obtener_respuesta_ia(st.session_state.messages)
            st.write(respuesta_bot)
            
    st.session_state.messages.append({"role": "assistant", "content": respuesta_bot})