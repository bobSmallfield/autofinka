import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="AutoFinka", layout="centered")
st.title("🏠 AutoFinka")
st.subheader("Generador automático de contratos inmobiliarios")

# Subida de logo y CSV
logo = "logo"
if not logo:
    st.markdown("### 📤 Sube el logo de tu inmobiliaria")
logo = st.file_uploader("Logo", type=["png", "jpg"])

st.markdown("### 📤 Sube la lista de agentes (CSV)")
csv_file = st.file_uploader("CSV de agentes", type=["csv"])

if logo and csv_file:
    df = pd.read_csv(csv_file)
    st.image(logo, width=200)

    st.markdown("### 🧾 Completa los datos del contrato")

    nombre_cliente = st.text_input("Nombre del cliente")
    direccion = st.text_input("Dirección de la propiedad")
    fecha = st.date_input("Fecha del contrato", value=datetime.today())

    if "nombre" in df.columns or "Nombre" in df.columns:
        col = "nombre" if "nombre" in df.columns else "Nombre"
        agente = st.selectbox("Selecciona agente responsable", df[col])
    else:
        st.error("⚠️ No se encontró una columna llamada 'nombre' o 'Nombre' en el CSV.")

  # Asegúrate de que la columna se llama 'nombre'

    if st.button("📄 Generar contrato PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Contrato de servicio inmobiliario", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Fecha: {fecha.strftime('%d/%m/%Y')}", ln=True)
        pdf.cell(200, 10, txt=f"Cliente: {nombre_cliente}", ln=True)
        pdf.cell(200, 10, txt=f"Dirección de la propiedad: {direccion}", ln=True)
        pdf.cell(200, 10, txt=f"Agente asignado: {agente}", ln=True)

        pdf_output = "contrato_autofinka.pdf"
        pdf.output(pdf_output)

        with open(pdf_output, "rb") as f:
            st.download_button(
                label="📥 Descargar contrato",
                data=f,
                file_name=pdf_output,
                mime="application/pdf"
            )
