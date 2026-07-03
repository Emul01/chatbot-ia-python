# 🤖 Chatbot de IA con Streamlit

Chatbot interactivo desarrollado con Python, Streamlit y la API de Groq (compatible con OpenAI), como proyecto para la asignatura de Cybersecurity - UTP.

Permite chatear con un modelo de lenguaje (Llama 3.3 70B) y, opcionalmente, subir un archivo `.txt` para darle contexto adicional a la IA antes de conversar.

## 🧩 Características

- Interfaz web interactiva construida con **Streamlit**.
- Lógica modularizada en funciones (`chatbot_utils.py`).
- Carga opcional de archivo `.txt` como contexto para el modelo.
- Manejo seguro de credenciales mediante variables de entorno (`.env`), excluidas del repositorio con `.gitignore`.

## 🛠️ Tecnologías

- Python 3.x
- Streamlit
- API de Groq (modelo `llama-3.3-70b-versatile`)
- python-dotenv

## 📦 Instalación

1. Clona el repositorio:
```bash
   git clone https://github.com/Emul01/chatbot-ia-python.git
   cd chatbot-ia-python
```

2. Crea y activa un entorno virtual:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```

3. Instala las dependencias:
```bash
   pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz del proyecto con tu API key de Groq:



> Puedes obtener una key gratuita en [console.groq.com](https://console.groq.com)

## ▶️ Uso

```bash
streamlit run app.py
```

Esto abrirá la aplicación en `http://localhost:8501`.

- Escribe directamente en el chat para conversar con la IA.
- Opcionalmente, sube un archivo `.txt` desde la barra lateral para que el bot use ese contenido como contexto en sus respuestas.

## 🔒 Seguridad

Las credenciales de API se manejan exclusivamente mediante variables de entorno (`.env`), el cual está excluido del control de versiones mediante `.gitignore` para evitar la exposición de tokens en el repositorio público.

## 📚 Recursos base

- [Python for AI - Full Beginner Course (Dave Ebbelaar)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
- [Documentación de funciones - Datalumina](https://python.datalumina.com/functions)