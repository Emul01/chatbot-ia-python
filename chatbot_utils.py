from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def obtener_respuesta_ia(historial_mensajes):
    """
    Interactúa con la API de OpenAI enviando el historial 
    de la conversación y retornando la respuesta del modelo.
    """
    try:
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=historial_mensajes,
            temperature=0.7
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        return f"Error al conectar con la IA: {str(e)}"


def procesar_archivo_contexto(archivo_subido):
    """
    Lee el contenido de un archivo de texto subido 
    para usarlo como contexto en el chatbot.
    """
    if archivo_subido is not None:
        try:
            contenido = archivo_subido.read().decode("utf-8")
            return contenido
        except Exception as e:
            return f"Error al leer el archivo: {str(e)}"
    return ""