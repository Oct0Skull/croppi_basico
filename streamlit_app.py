import streamlit as st

st.title("🏃‍♂️💨 Croppi app")

# mensaje de bienvenida por default
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# ejemplo tomado de Youtube
cantidad = st.slider('Seleccionar la cantidad:')

st.write('La cantidad seleccionada es: {cantidad}')

# se eneran una cantidad de botones de acuerdo al numero colocado
for i in range(cantidad):
    st.button(f'boton {i+1}')