import streamlit as st

st.set_page_config(page_title="Autofinka", layout="wide")

st.title("🏠 Autofinka")
st.subheader("Automatiza contratos inmobiliarios con estilo.")

st.write("👋 Bienvenido a la demo. Aquí podrás subir tu logo, cargar tus agentes y generar un contrato en PDF personalizado.")

uploaded_logo = st.file_uploader("Sube tu logo", type=["png", "jpg"])
uploaded_csv = st.file_uploader("Sube tu lista de agentes", type=["csv"])

if uploaded_logo:
    st.image(uploaded_logo, width=200)

if uploaded_csv:
    import pandas as pd
    df = pd.read_csv(uploaded_csv)
    st.write("Agentes cargados:")
    st.dataframe(df)
