import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Reproductor MP3", 
    page_icon="🎵", 
    layout="centered"
)

# Título y descripción de la aplicación
st.title("🎵 Reproductor de Música MP3")
st.markdown("Sube tus archivos de audio en formato **MP3** y escúchalos directamente desde tu navegador.")

st.divider()

# Widget para subir archivos (permite múltiples archivos)
uploaded_files = st.file_uploader(
    "Selecciona uno o más archivos MP3", 
    type=["mp3"], 
    accept_multiple_files=True
)

# Lógica principal del reproductor
if uploaded_files:
    # Mostrar mensaje de éxito si se cargan archivos
    st.success(f"Se han cargado {len(uploaded_files)} archivo(s) correctamente.")
    
    # Crear un diccionario para mapear los nombres de los archivos con los objetos cargados
    canciones = {file.name: file for file in uploaded_files}
    
    # Selector de canciones
    st.subheader("Lista de reproducción")
    cancion_seleccionada = st.selectbox(
        "Elige la canción que deseas escuchar:", 
        options=list(canciones.keys())
    )
    
    # Reproductor de audio
    if cancion_seleccionada:
        st.write(f"▶️ **Reproduciendo ahora:** {cancion_seleccionada}")
        
        # Streamlit lee el archivo directamente del buffer de memoria
        archivo_audio = canciones[cancion_seleccionada]
        st.audio(archivo_audio, format='audio/mp3')
        
        # Mostrar información extra (tamaño del archivo en MB)
        tamano_mb = archivo_audio.size / (1024 * 1024)
        st.caption(f"Tamaño del archivo: {tamano_mb:.2f} MB")

else:
    # Mensaje por defecto cuando no hay archivos
    st.info("👆 Por favor, sube uno o más archivos MP3 usando el botón de arriba para comenzar a escuchar música.")