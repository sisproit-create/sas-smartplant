import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SAS SmartPlant Demo",
    page_icon="🏭",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

body {
    background-color: #111827;
    color: #e5e7eb;
}

.stApp {
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    color: #e5e7eb;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
}

div[data-testid="stToolbar"] {
    right: 0.5rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.block-container {
    padding-top: 3.8rem;
    padding-bottom: 1rem;
    max-width: 95rem;
}

.sas-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 0.8rem;
    margin-bottom: 0.2rem;
    letter-spacing: -0.02em;
    line-height: 1.1;
    word-break: break-word;
}

.sas-sub {
    color: #cbd5e1;
    margin-bottom: 1.4rem;
    font-size: 1.02rem;
    line-height: 1.6;
}

h1, h2, h3, h4 {
    color: #f9fafb !important;
}

p, div, span, label {
    color: #d1d5db !important;
}

[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 18px;
    padding: 16px 18px;
}

[data-testid="stMetricLabel"] {
    color: #9ca3af !important;
    font-size: 0.95rem !important;
}

[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-weight: 700 !important;
}

[data-testid="stMetricDelta"] {
    font-weight: 700 !important;
    font-size: 1rem !important;
    border-radius: 999px;
    padding: 4px 10px;
    display: inline-flex;
    width: fit-content;
    background-color: rgba(15, 118, 110, 0.22) !important;
    color: #6ee7b7 !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.15);
}

.stTabs [data-baseweb="tab"] {
    color: #cbd5e1;
    font-weight: 500;
}

.stTabs [aria-selected="true"] {
    color: #38bdf8 !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 14px;
    overflow: hidden;
}

.alert-red {
    background: rgba(127, 29, 29, 0.45);
    border-left: 5px solid #ef4444;
    padding: 12px;
    border-radius: 12px;
    color: #fecaca !important;
    margin-bottom: 10px;
    line-height: 1.55;
}

.alert-yellow {
    background: rgba(120, 53, 15, 0.35);
    border-left: 5px solid #f59e0b;
    padding: 12px;
    border-radius: 12px;
    color: #fde68a !important;
    margin-bottom: 10px;
    line-height: 1.55;
}

.alert-green {
    background: rgba(20, 83, 45, 0.35);
    border-left: 5px solid #22c55e;
    padding: 12px;
    border-radius: 12px;
    color: #bbf7d0 !important;
    margin-bottom: 10px;
    line-height: 1.55;
}

div[data-testid="stAlert"] {
    background-color: rgba(30, 41, 59, 0.72) !important;
    border: 1px solid rgba(148, 163, 184, 0.12) !important;
    color: #e5e7eb !important;
    border-radius: 12px !important;
}

hr {
    border-color: rgba(148, 163, 184, 0.15) !important;
}

[data-testid="stCaptionContainer"] {
    color: #94a3b8 !important;
}

@media (max-width: 768px) {
    .sas-title {
        font-size: 1.55rem;
        margin-top: 1rem;
        line-height: 1.2;
    }

    .sas-sub {
        font-size: 0.95rem;
        line-height: 1.6;
    }

    [data-testid="stMetric"] {
        padding: 16px;
        border-radius: 20px;
    }

    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

diesel_flow = pd.DataFrame({
    "Etapa": ["Recepción P2", "Despacho Hyundai", "Distribución Equipos", "Diferencia"],
    "Valor": [10000, 8500, 8200, 300]
})

ac30_data = pd.DataFrame({
    "Concepto": ["Inventario inicial", "Recepción", "Consumo", "Inventario final"],
    "Kg": [60000, 20000, 52000, 28000]
})

prod_history = pd.DataFrame({
    "Fecha": pd.date_range("2026-03-14", periods=7, freq="D"),
    "Toneladas": [1480, 1625, 1590, 1734, 1680, 1710, 1655],
    "Diesel_gal": [3900, 4100, 4050, 4700, 4380, 4450, 4325]
})
prod_history["gal_ton"] = (prod_history["Diesel_gal"] / prod_history["Toneladas"]).round(2)

equipos = pd.DataFrame({
    "Equipo": ["Generador P2", "Cargador SEM 636D", "Pala Doosan", "Torre de Luz 1", "Pick Up CE9798"],
    "Galones": [1200, 1600, 1450, 220, 180]
})

st.markdown('<div class="sas-title">SAS SmartPlant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sas-sub">Control inteligente de diésel, AC30, producción y alertas en tiempo real</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Producción", "1,734 ton", "+9.1%")
col2.metric("Diésel", "4,700 gal", "+14.8%")
col3.metric("AC30", "52,000 kg", "-500 kg")
col4.metric("Costo diésel / ton", "2.71", "+0.95")
col5.metric("Alertas", "3", "+2")

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Resumen Ejecutivo",
    "Diésel",
    "AC30",
    "Producción",
    "Alertas"
])

with tab1:
    left, right = st.columns([1.3, 1])

    with left:
        st.subheader("KPIs clave del día")

        fig = px.line(
            prod_history,
            x="Fecha",
            y="Toneladas",
            markers=True,
            title="Toneladas producidas (7 días)"
        )
        fig.update_layout(
            template="plotly_white",
            height=330,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="#f8fafc",
            plot_bgcolor="#f8fafc",
            font=dict(color="#111827")
        )
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.bar(
            equipos,
            x="Equipo",
            y="Galones",
            title="Distribución de diésel por equipo"
        )
        fig2.update_layout(
            template="plotly_white",
            height=330,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="#f8fafc",
            plot_bgcolor="#f8fafc",
            font=dict(color="#111827")
        )
        st.plotly_chart(fig2, use_container_width=True)

    with right:
        st.subheader("Estado operativo")
        st.markdown('<div class="alert-red"><b>Alerta roja:</b> La diferencia entre despacho Hyundai y distribución a equipos es de 300 gal.</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-yellow"><b>Alerta amarilla:</b> El consumo de diésel por tonelada está 18% por encima del promedio de los últimos 7 días.</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-yellow"><b>AC30:</b> Se detecta una diferencia de -500 kg frente al inventario esperado.</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-green"><b>Producción:</b> La planta operó con 1,734 ton en el día y mantuvo continuidad de despacho.</div>', unsafe_allow_html=True)

        st.subheader("Recomendación del sistema")
        st.info("Revisar humedad de agregados, tiempos muertos, temperatura de operación y conciliación del flujo P2 → Hyundai → Equipos antes del cierre diario.")

with tab2:
    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("Flujo de diésel")
        fig = px.funnel(
            diesel_flow,
            x="Valor",
            y="Etapa",
            title="P2 → Hyundai → Equipos"
        )
        fig.update_layout(
            template="plotly_white",
            height=380,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="#f8fafc",
            plot_bgcolor="#f8fafc",
            font=dict(color="#111827")
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Conciliación")
        st.dataframe(diesel_flow, use_container_width=True, hide_index=True)
        st.write("**Validación automática**")
        st.write("- Recepción P2: 10,000 gal")
        st.write("- Despacho a Hyundai: 8,500 gal")
        st.write("- Distribución a equipos: 8,200 gal")
        st.write("- Diferencia detectada: 300 gal")
        st.error("Estado: ALERTA ROJA")

with tab3:
    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("Balance AC30")
        fig = px.bar(
            ac30_data,
            x="Concepto",
            y="Kg",
            title="Inventario y consumo AC30"
        )
        fig.update_layout(
            template="plotly_white",
            height=380,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="#f8fafc",
            plot_bgcolor="#f8fafc",
            font=dict(color="#111827")
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Resumen AC30")
        st.dataframe(ac30_data, use_container_width=True, hide_index=True)
        st.write("**Lectura inteligente**")
        st.write("- Inventario inicial: 60,000 kg")
        st.write("- Recepción: 20,000 kg")
        st.write("- Consumo: 52,000 kg")
        st.write("- Inventario final: 28,000 kg")
        st.warning("Diferencia estimada: -500 kg")

with tab4:
    c1, c2 = st.columns([1.2, 1])

    with c1:
        st.subheader("Tendencia operativa")
        fig = px.line(
            prod_history,
            x="Fecha",
            y="gal_ton",
            markers=True,
            title="Consumo de diésel por tonelada"
        )
        fig.update_layout(
            template="plotly_white",
            height=380,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="#f8fafc",
            plot_bgcolor="#f8fafc",
            font=dict(color="#111827")
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Resumen de eficiencia")
        st.metric("Consumo actual", "2.71 gal/ton")
        st.metric("Meta operativa", "1.80 gal/ton")
        st.metric("Desviación", "+50%")
        st.write("**Interpretación**")
        st.write("El sistema detecta una desviación relevante frente a la meta operativa.")
        st.write("Se recomienda validar tiempos muertos, humedad del material y temperatura de operación.")

with tab5:
    st.subheader("Panel de alertas inteligentes")
    st.markdown('<div class="alert-red"><b>1. Sobreconsumo de diésel</b><br>El consumo por tonelada subió a 2.71 vs meta de 1.80.</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert-red"><b>2. Diferencia en flujo de combustible</b><br>La suma distribuida a equipos no cuadra con el despacho al Hyundai.</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert-yellow"><b>3. AC30 fuera de balance</b><br>El inventario final real no coincide con el estimado teórico.</div>', unsafe_allow_html=True)

    st.subheader("Acciones sugeridas por SAS SmartPlant")
    st.write("1. Revisar registro físico del despacho a Hyundai.")
    st.write("2. Confirmar si existe distribución pendiente no registrada.")
    st.write("3. Validar nivel final de AC30 y corregir conciliación.")
    st.write("4. Revisar causas de sobreconsumo antes de la siguiente jornada.")

st.divider()
st.caption("SAS SmartPlant • Demo para inversionistas")
