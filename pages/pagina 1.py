# pages/introduccion.py
import streamlit as st

st.title("📚 Introducción")
st.markdown("Bienvenido a la **Introducción** de nuestra aventura. Aquí descubrirás lo que te espera en este viaje.")
st.write("Pero espera... ¡hay algo de magia en el aire!")

# Botones interactivos
col1, col2 = st.columns(2)
with col1:
    if st.button("Quiero saber más 🤓"):
        st.info("Este proyecto está diseñado para hacerte sonreír, aprender algo nuevo y, quién sabe, ¡quizás dejarte un poco inspirado!")

with col2:
    if st.button("Muéstrame algo genial 🎩"):
        st.markdown("![Wow](https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif)")
        st.write("¿Genial, verdad? ¡Sigamos explorando! 🔍")
