import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="AutoFinka", layout="centered")
st.title("🏠 AutoFinka")
st.subheader("Generador automático de contratos inmobiliarios")

# Subida de logo y CSV
logo = 0
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
        with open("plantillas/contrato_base.txt", "r", encoding="utf-8") as file:
            plantilla = file.read()

        # Datos dinámicos (los que vienen del form de Streamlit)
        datos = {
            "ciudad": "Madrid",
            "fecha": fecha,
            "nombre_cliente": nombre_cliente,
            "dni_cliente": "12345678A",
            "nombre_agente": "María Gómez",
            "direccion": direccion,
            "precio": "250000",
            "duracion": "6"
        }

        # Sustituir variables
        for clave, valor in datos.items():
            plantilla = plantilla.replace("{" + str(clave) + "}", str(valor))
        
        pdf_output = "contrato_1"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Añadir línea a línea
        for linea in plantilla.splitlines():
            pdf.multi_cell(0, 10, linea)
            pdf.ln(2)  # Espacio entre párrafos

        pdf.output(pdf_output)

        with open(pdf_output, "rb") as f:
            st.download_button(
                label="📥 Descargar contrato",
                data=f,
                file_name=pdf_output,
                mime="application/pdf"
            )
