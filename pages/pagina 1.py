# app.py
import streamlit as st
pip install streamlit-option-menu
streamlit run app.py


from streamlit_option_menu import option_menu

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
