import streamlit as st
import requests
import io
import pygame
from pygame import mixer
from st_social_media_links import SocialMediaIcons

# Inicializa el mezclador de audio
mixer.init()

# Diccionario de voces con su respectivo ID
VOCES = {
    "Juan Carlos": "YExhVa4bZONzeingloMX",
    "Santiago": "15bJsujCI3tcDWeoZsQP",
    "Sarah": "EXAVITQu4vr4xnSDxMaL"}

# Función para solicitar el audio desde la API de Eleven Labs
def obtener_audio(texto, voz, api_key):
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{VOCES[voz]}'
    headers = {'Content-Type': 'application/json', 'xi-api-key': api_key}
    data = {
        'text': texto,
        'voice_settings': {'stability': 0.3, 'similarity_boost': 0.8},
        'language': 'es'  # Indicar idioma español
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        st.error(f"Error al obtener el audio: {response.text}")
        return None

# Función para reproducir el audio
def reproducir_audio(audio_stream):
    mixer.music.load(audio_stream, 'mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Cargar y mostrar el logo en la esquina superior izquierda
logo_path = "https://cdn-icons-gif.flaticon.com/12320/12320079.gif" 
st.image(logo_path, width=100)  # Ajusta el ancho del logo según sea necesario

# Interfaz en Streamlit
st.title("Traductor de Texto a Voz")
st.write("Ingrese su clave API de Eleven Labs y elija una voz para convertir texto a voz en español.")

# Entrada para la clave API
api_key = st.text_input("API Key de Eleven Labs", type="password")

# Verificación de la clave API
if api_key:
    # Entrada para el texto
    texto = st.text_area("Texto a traducir")
    
    # Selector de voz
    voz_seleccionada = st.selectbox("Seleccione la voz", list(VOCES.keys()))
    
    # Botón para generar y reproducir el audio
    if st.button("Traducir y reproducir"):
        audio_stream = obtener_audio(texto, voz_seleccionada, api_key)
        
        if audio_stream:
            reproducir_audio(audio_stream)
            st.success("Reproducción en curso...")
else:
    st.warning("Por favor, ingrese su clave API para continuar.")

# Pie de página con información del desarrollador y logos de redes sociales
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate<br>
**Email:** egqa1975@gmail.com<br>
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()