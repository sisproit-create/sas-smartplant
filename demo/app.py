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

/* ===== Base ===== */
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

/* ===== Ocultar barra superior ===== */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
}

div[data-testid="stToolbar"] {
    right: 0.5rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ===== Contenedor ===== */
.block-container {
    padding-top: 3.8rem;
    padding-bottom: 1rem;
    max-width: 95rem;
}

/* ===== Título ===== */
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

/* ===== Texto ===== */
h1, h2, h3, h4 {
    color: #f9fafb !important;
}

p, div, span, label {
    color: #d1d5db !important;
}

/* ===== Métricas ===== */
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

/* ===== Delta ===== */
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

/* ===== Tabs ===== */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.15);
}

.stTabs [data-baseweb="tab"] {
    color: #cbd5e1;
}

.stTabs [aria-selected="true"] {
    color: #38bdf8 !important;
}

/* ===== Alertas ===== */
.alert-red {
    background: rgba(127, 29, 29, 0.45);
    border-left: 5px solid #ef4444;
    padding: 12px;
    border-radius: 12px;
    color: #fecaca !important;
    margin-bottom: 10px;
}

.alert-yellow {
    background: rgba(120, 53, 15, 0.35);
    border-left: 5px solid #f59e0b;
    padding: 12px;
    border-radius: 12px;
    color: #fde68a !important;
    margin-bottom: 10px;
}

.alert-green {
    background: rgba(20, 83, 45, 0.35);
    border-left: 5px solid #22c55e;
    padding: 12px;
    border-radius: 12px;
    color: #bbf7d0 !important;
    margin-bottom: 10px;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {

    .sas-title {
        font-size: 1.55rem;
        margin-top: 1rem;
    }

    .sas-sub {
        font-size: 0.95rem;
    }

    [data-testid="stMetric"] {
        padding: 16px;
    }

    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ===== DATA =====
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
    "Equipo": ["Generador P2", "Cargador SEM", "Pala Doosan", "Torre de Luz", "Pick Up"],
    "Galones": [1200, 1600, 1450, 220, 180]
})

# ===== HEADER =====
st.markdown('<div class="sas-title">SAS SmartPlant</div>', unsafe_allow_html=True)
st.markdown('<div class="sas-sub">Control inteligente de diésel, AC30, producción y alertas en tiempo real</div>', unsafe_allow_html=True)

# ===== KPIs =====
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Producción", "1,734 ton", "+9.1%")
col2.metric("Diésel", "4,700 gal", "+14.8%")
col3.metric("AC30", "52,000 kg", "-500 kg")
col4.metric("Costo diésel / ton", "2.71", "+0.95")
col5.metric("Alertas", "3", "+2")

st.divider()

# ===== TABS =====
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
        st.subheader("KPIs clave")

        fig = px.line(prod_history, x="Fecha", y="Toneladas", markers=True)
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Estado")

        st.markdown('<div class="alert-red">Diferencia de 300 gal detectada</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-yellow">Consumo alto de diésel</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-green">Producción estable</div>', unsafe_allow_html=True)

with tab2:
    st.dataframe(diesel_flow)

with tab3:
    st.dataframe(ac30_data)

with tab4:
    fig = px.line(prod_history, x="Fecha", y="gal_ton")
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.markdown('<div class="alert-red">Sobreconsumo detectado</div>', unsafe_allow_html=True)

st.caption("SAS SmartPlant • Demo para inversionistas")
