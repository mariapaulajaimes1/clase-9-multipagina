# pages/inicio.py
import streamlit as st

st.title("🎉 Bienvenidos a la Aventura Interactiva 🎉")
st.write("¿Estás listo para embarcarte en una experiencia inolvidable? ¡Sujeta tu cinturón y disfruta del viaje!")

st.markdown("## Vamos a Empezar 🚀")
st.write("Para continuar, pulsa el botón mágico aquí abajo 👇")

# Botón de inicio con interacción
if st.button("Presiona Aquí para una Sorpresa 🎁"):
    st.balloons()
    st.success("¡Eso fue divertido! Ahora, veamos qué tenemos en la **Introducción**.")

