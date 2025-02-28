import streamlit as st

st.title("WealthMap:Tu patrimonio blindado y en el camino correcto")
st.write("Bienvenido al primer portal que evalúa tu situación, anticipa riesgos y encuentra la estrategia ideal para fortalecer tu patrimonio. Convierte la incertidumbre en estrategia. ")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Configuración de rentabilidad e inflación
RENTABILIDAD_ANUAL = 0.09  # 9%
INFLACION_ANUAL = 0.02  # 2%

# Lista de riesgos patrimoniales
RIESGOS = [
    "Sistema financiero local",
    "Sistema fiscal",
    "Transferencia patrimonial (Divorcio, disolución de un vínculo, herencia)",
    "Incertidumbre civil",
    "Crisis política",
    "Inflación",
    "Inseguridad jurídica",
    "Débil sistema previsional"
]

# Función para proyectar patrimonio futuro
def proyectar_patrimonio(patrimonio_inicial, años):
    valores = []
    for i in range(años):
        patrimonio_inicial *= (1 + RENTABILIDAD_ANUAL - INFLACION_ANUAL)
        valores.append(patrimonio_inicial)
    return valores

# Interfaz de usuario
st.title("Simulador de Planificación Patrimonial")

# Ingreso de datos
nombre = st.text_input("Nombre del usuario")
edad = st.number_input("Edad", min_value=18, max_value=100, value=35)
dependientes = st.number_input("Número de dependientes", min_value=0, value=0)
ingresos_anuales = st.number_input("Ingresos anuales (USD)", min_value=0, value=50000)
activos_inmobiliarios = st.number_input("Valor de activos inmobiliarios (USD)", min_value=0, value=200000)
activos_financieros = st.number_input("Valor de activos financieros (USD)", min_value=0, value=50000)
activos_juridicos = st.number_input("Valor de activos jurídicos (USD)", min_value=0, value=30000)
vehiculos = st.number_input("Valor de vehículos (USD)", min_value=0, value=20000)
edad_retiro = st.number_input("Edad deseada de retiro", min_value=40, max_value=80, value=65)
ingreso_deseado_retiro = st.number_input("Ingreso anual deseado en retiro (USD)", min_value=0, value=30000)

# Selección de riesgos
st.subheader("Riesgos Patrimoniales")
riesgos_seleccionados = st.multiselect("Seleccione los riesgos a los que se enfrenta:", RIESGOS)

# Cálculo de patrimonio total
patrimonio_total = activos_inmobiliarios + activos_financieros + activos_juridicos + vehiculos
st.write(f"### Patrimonio total actual: ${patrimonio_total:,.2f}")

# Simulación de escenarios
st.subheader("Proyección Patrimonial")
años_proyeccion = st.slider("Seleccione el número de años para la proyección:", 5, 30, 10)
proyeccion_patrimonio = proyectar_patrimonio(patrimonio_total, años_proyeccion)

# Gráfico de evolución del patrimonio
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(edad, edad + años_proyeccion), proyeccion_patrimonio, marker='o', linestyle='-', color='b')
ax.set_xlabel("Edad")
ax.set_ylabel("Patrimonio proyectado (USD)")
ax.set_title("Evolución del Patrimonio en el Tiempo")
ax.grid()
st.pyplot(fig)

# Conclusiones y Recomendaciones
st.subheader("Recomendaciones Personalizadas")
if patrimonio_total < ingreso_deseado_retiro * 20:
    st.write("⚠️ Considera aumentar tus inversiones para asegurar tu retiro.")
if "Inflación" in riesgos_seleccionados:
    st.write("⚠️ Diversificar tus inversiones en activos que protejan contra la inflación.")
if "Débil sistema previsional" in riesgos_seleccionados:
    st.write("⚠️ Explora opciones de planes de pensiones privados para asegurar tu futuro.")

st.write("Este simulador es una herramienta de orientación. Consulta con un asesor financiero para estrategias personalizadas.")
