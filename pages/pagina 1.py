# app.py
import streamlit as st

# Intentar importar la librería y agregar instrucción de instalación si no está instalada
try:
    from streamlit_option_menu import option_menu
except ModuleNotFoundError:
    st.error("La librería 'streamlit-option-menu' no está instalada. Ejecútalo en la terminal con el comando: `pip install streamlit-option-menu`")
    st.stop()

# Configuración de página
st.set_page_config(page_title="Aplicación Divertida", page_icon="🎉")

# Menú de navegación en la barra lateral
with st.sidebar:
    seleccion = option_menu("Menú de Navegación", ["Inicio", "Introducción"],
                            icons=['house', 'info-circle'],
                            menu_icon="cast", default_index=0)

# Lógica de navegación
if seleccion == "Inicio":
    import pages.inicio

elif seleccion == "Introducción":
    import pages.introduccion
