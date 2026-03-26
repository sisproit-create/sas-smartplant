import streamlit as st
import pandas as pd
import numpy as np
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

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

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


# =========================
# DATA DEMO
# =========================
prod_history = pd.DataFrame({
    "Fecha": pd.to_datetime([
        "2026-03-14", "2026-03-16", "2026-03-17",
        "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-24"
    ]),
    "Tipo_Mezcla": ["IV-B", "IV-B", "IV-B", "IV-B", "IV-B", "IV-B", "IV-B"],
    "Toneladas": [274.15, 269.62, 272.69, 122.06, 371.70, 22.00, 50.01],
    "Diesel_gal": [498.30, 549.33, 556.11, 254.07, 685.75, 115.90, 103.40],
    "Diesel_gal_ton": [1.82, 2.04, 2.04, 2.08, 1.84, 5.27, 2.07],
    "Asfalto_AC30_gal": [3548.56, 3908.96, 3576.28, 1580.22, 5017.88, 221.78, 748.52],
    "Contenido_Asfalto_AC30_kg": [13701.00, 15092.49, 13808.01, 6101.22, 19374.04, 856.31, 2890.05],
    "Consumo_Asfalto_AC30_gl_ton": [12.94, 14.50, 13.11, 12.95, 13.50, 10.08, 14.97],
    "Contenido_Asfalto_AC30_kg_ton": [49.97, 55.98, 50.64, 49.99, 52.12, 38.92, 57.79]
})

diesel_flow = pd.DataFrame({
    "Etapa": ["Recepción P2", "Despacho a Hyundai", "Distribución a Equipos", "Diferencia"],
    "Valor": [10000, 8500, 8200, 300]
})

equipos = pd.DataFrame({
    "Equipo": ["Generador P2", "Cargador SEM 636D", "Pala Doosan", "Torre de Luz 1", "Pick Up CE9798"],
    "Galones": [1200, 1600, 1450, 220, 180]
})

ac30_inventory = pd.DataFrame({
    "Concepto": [
        "Inventario inicial",
        "Recepción",
        "Asfalto (AC30) usado",
        "Inventario final",
        "Diferencia teórica vs real"
    ],
    "Kg": [60000, 20000, 52000, 28000, -500]
})

mezclas = pd.DataFrame({
    "Tipo de mezcla": ["IV-B", "MS-22", "Base", "Binder"],
    "Toneladas": [800, 500, 250, 184]
})

calidad_data = pd.DataFrame({
    "Parámetro": ["Contenido de asfalto %", "Densidad", "Vacíos", "Estabilidad", "Flujo"],
    "Diseño": [5.5, 2.35, 4.0, 1200, 3.5],
    "Real": [5.8, 2.30, 4.8, 1100, 3.9],
    "Cumplimiento": ["⚠️ Parcial", "❌ No cumple", "⚠️ Parcial", "❌ No cumple", "⚠️ Parcial"]
})


# =========================
# HELPERS
# =========================
def plot_white_layout(fig, height=340):
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor="#f8fafc",
        plot_bgcolor="#f8fafc",
        font=dict(color="#111827"),
        legend_title_text=""
    )
    return fig


def render_html_alert(message: str, level: str = "yellow"):
    css_class = {
        "red": "alert-red",
        "yellow": "alert-yellow",
        "green": "alert-green"
    }.get(level, "alert-yellow")

    st.markdown(f'<div class="{css_class}">{message}</div>', unsafe_allow_html=True)


def build_diesel_alerts(
    df: pd.DataFrame,
    target_gal_ton: float = 1.80,
    tol_gal_ton: float = 0.25
) -> pd.DataFrame:
    alerts = []

    for _, row in df.iterrows():
        fecha_txt = row["Fecha"].strftime("%Y-%m-%d")
        delta = row["Diesel_gal_ton"] - target_gal_ton

        if abs(delta) > tol_gal_ton:
            level = "🚨 Alta" if abs(delta) > (tol_gal_ton * 2) else "⚠️ Media"
            alerts.append({
                "Fecha": fecha_txt,
                "Tipo": "Desviación de Consumo de Combustible Diésel – gal/ton",
                "Nivel": level,
                "Valor": round(row["Diesel_gal_ton"], 2),
                "Meta": target_gal_ton,
                "Delta": round(delta, 2),
                "Mensaje": f"Consumo de Combustible Diésel fuera de rango: {row['Diesel_gal_ton']:.2f} gal/ton vs meta {target_gal_ton:.2f}"
            })

        if row["Toneladas"] < 25:
            alerts.append({
                "Fecha": fecha_txt,
                "Tipo": "Producción baja",
                "Nivel": "ℹ️ Info",
                "Valor": round(row["Toneladas"], 2),
                "Meta": 25,
                "Delta": round(row["Toneladas"] - 25, 2),
                "Mensaje": f"Producción baja ({row['Toneladas']:.2f} ton). Revisar este dato con cautela."
            })

    alerts_df = pd.DataFrame(alerts)
    if alerts_df.empty:
        return pd.DataFrame(columns=["Fecha", "Tipo", "Nivel", "Valor", "Meta", "Delta", "Mensaje"])

    order = {"🚨 Alta": 0, "⚠️ Media": 1, "ℹ️ Info": 2}
    alerts_df["sort"] = alerts_df["Nivel"].map(order).fillna(99)
    return alerts_df.sort_values(["sort", "Fecha"]).drop(columns=["sort"]).reset_index(drop=True)


def build_ac30_alerts(
    df: pd.DataFrame,
    target_kg_ton: float = 52.0,
    tol_kg_ton: float = 3.0
) -> pd.DataFrame:
    alerts = []

    target_gl_ton = target_kg_ton / 3.861
    tol_gl_ton = tol_kg_ton / 3.861

    for _, row in df.iterrows():
        fecha_txt = row["Fecha"].strftime("%Y-%m-%d")

        delta_kg = row["Contenido_Asfalto_AC30_kg_ton"] - target_kg_ton
        if abs(delta_kg) > tol_kg_ton:
            level = "🚨 Alta" if abs(delta_kg) > (tol_kg_ton * 2) else "⚠️ Media"
            alerts.append({
                "Fecha": fecha_txt,
                "Tipo": "Desviación de Contenido de Asfalto (AC30) – kg/ton",
                "Nivel": level,
                "Valor": round(row["Contenido_Asfalto_AC30_kg_ton"], 2),
                "Meta": target_kg_ton,
                "Delta": round(delta_kg, 2),
                "Mensaje": f"Contenido de Asfalto (AC30) fuera de rango: {row['Contenido_Asfalto_AC30_kg_ton']:.2f} kg/ton vs meta {target_kg_ton:.2f}"
            })

        delta_gl = row["Consumo_Asfalto_AC30_gl_ton"] - target_gl_ton
        if abs(delta_gl) > tol_gl_ton:
            level = "🚨 Alta" if abs(delta_gl) > (tol_gl_ton * 2) else "⚠️ Media"
            alerts.append({
                "Fecha": fecha_txt,
                "Tipo": "Desviación de Consumo de Asfalto (AC30) – gl/ton",
                "Nivel": level,
                "Valor": round(row["Consumo_Asfalto_AC30_gl_ton"], 2),
                "Meta": round(target_gl_ton, 2),
                "Delta": round(delta_gl, 2),
                "Mensaje": f"Consumo de Asfalto (AC30) fuera de rango: {row['Consumo_Asfalto_AC30_gl_ton']:.2f} gl/ton vs meta {target_gl_ton:.2f}"
            })

        if row["Toneladas"] < 25:
            alerts.append({
                "Fecha": fecha_txt,
                "Tipo": "Producción baja",
                "Nivel": "ℹ️ Info",
                "Valor": round(row["Toneladas"], 2),
                "Meta": 25,
                "Delta": round(row["Toneladas"] - 25, 2),
                "Mensaje": f"Producción baja ({row['Toneladas']:.2f} ton). Revisar este dato con cautela."
            })

    alerts_df = pd.DataFrame(alerts)
    if alerts_df.empty:
        return pd.DataFrame(columns=["Fecha", "Tipo", "Nivel", "Valor", "Meta", "Delta", "Mensaje"])

    order = {"🚨 Alta": 0, "⚠️ Media": 1, "ℹ️ Info": 2}
    alerts_df["sort"] = alerts_df["Nivel"].map(order).fillna(99)
    return alerts_df.sort_values(["sort", "Fecha"]).drop(columns=["sort"]).reset_index(drop=True)


def render_resumen_operacional(df: pd.DataFrame):
    st.subheader("Tendencia operacional")

    TARGET_DIESEL = 1.80
    TOL_DIESEL = 0.25

    TARGET_AC30 = 52.0
    TOL_AC30 = 3.0

    g1, g2, g3 = st.columns(3)

    with g1:
        fig_prod = px.line(
            df,
            x="Fecha",
            y="Toneladas",
            markers=True,
            title="Producción – ton/día"
        )
        st.plotly_chart(plot_white_layout(fig_prod, height=300), use_container_width=True)

        low_prod = df[df["Toneladas"] < 50]
        if not low_prod.empty:
            for _, row in low_prod.iterrows():
                st.warning(f"{row['Fecha'].strftime('%d %b')} → Producción baja: {row['Toneladas']:.2f} ton")

    with g2:
        fig_diesel = px.line(
            df,
            x="Fecha",
            y="Diesel_gal_ton",
            markers=True,
            title="Consumo de Combustible Diésel – gal/ton"
        )
        fig_diesel.add_hline(y=TARGET_DIESEL, line_dash="dash", annotation_text="Meta")
        fig_diesel.add_hline(y=TARGET_DIESEL + TOL_DIESEL, line_dash="dot")
        fig_diesel.add_hline(y=TARGET_DIESEL - TOL_DIESEL, line_dash="dot")
        st.plotly_chart(plot_white_layout(fig_diesel, height=300), use_container_width=True)

        high_diesel = df[df["Diesel_gal_ton"] > TARGET_DIESEL + TOL_DIESEL]
        low_diesel = df[df["Diesel_gal_ton"] < TARGET_DIESEL - TOL_DIESEL]

        if not high_diesel.empty:
            for _, row in high_diesel.iterrows():
                st.warning(f"{row['Fecha'].strftime('%d %b')} → Sobreconsumo de diésel")
        elif not low_diesel.empty:
            for _, row in low_diesel.iterrows():
                st.info(f"{row['Fecha'].strftime('%d %b')} → Bajo consumo de diésel")
        else:
            st.success("Diésel dentro del rango esperado.")

    with g3:
        fig_ac30 = px.line(
            df,
            x="Fecha",
            y="Contenido_Asfalto_AC30_kg_ton",
            markers=True,
            title="Contenido de Asfalto (AC30) – kg/ton"
        )
        fig_ac30.add_hline(y=TARGET_AC30, line_dash="dash", annotation_text="Meta diseño")
        fig_ac30.add_hline(y=TARGET_AC30 + TOL_AC30, line_dash="dot")
        fig_ac30.add_hline(y=TARGET_AC30 - TOL_AC30, line_dash="dot")
        st.plotly_chart(plot_white_layout(fig_ac30, height=300), use_container_width=True)

        high_ac30 = df[df["Contenido_Asfalto_AC30_kg_ton"] > TARGET_AC30 + TOL_AC30]
        low_ac30 = df[df["Contenido_Asfalto_AC30_kg_ton"] < TARGET_AC30 - TOL_AC30]

        if not high_ac30.empty:
            for _, row in high_ac30.iterrows():
                st.error(f"{row['Fecha'].strftime('%d %b')} → Exceso de asfalto")
        if not low_ac30.empty:
            for _, row in low_ac30.iterrows():
                st.warning(f"{row['Fecha'].strftime('%d %b')} → Bajo contenido de asfalto")
        if high_ac30.empty and low_ac30.empty:
            st.success("AC30 dentro del diseño esperado.")


def render_diesel_module(
    df: pd.DataFrame,
    diesel_flow_df: pd.DataFrame,
    equipos_df: pd.DataFrame,
    target_gal_ton: float = 1.80,
    tol_gal_ton: float = 0.25,
    diesel_price_per_gal: float = 4.30
):
    st.subheader("⛽ Módulo de Consumo de Combustible Diésel")
    st.markdown("""
    ### 🎯 Qué responde este módulo
    - ¿Estamos cumpliendo la meta de consumo de Combustible Diésel?
    - ¿Qué días hubo sobreconsumo?
    - ¿Cuál fue el impacto económico del exceso?
    - ¿Hay desbalance entre recepción, despacho y distribución?
    """)

    diesel_df = df.copy().sort_values("Fecha").reset_index(drop=True)
    diesel_df["Toneladas_Acumuladas"] = diesel_df["Toneladas"].cumsum()
    diesel_df["Diesel_Acumulado_gal"] = diesel_df["Diesel_gal"].cumsum()
    diesel_df["Consumo_Diesel_Acumulado_gal_ton"] = np.where(
        diesel_df["Toneladas_Acumuladas"] > 0,
        diesel_df["Diesel_Acumulado_gal"] / diesel_df["Toneladas_Acumuladas"],
        np.nan
    )

    alerts_df = build_diesel_alerts(diesel_df, target_gal_ton, tol_gal_ton)

    total_ton = diesel_df["Toneladas"].sum()
    total_diesel = diesel_df["Diesel_gal"].sum()
    avg_diesel_gal_ton = total_diesel / total_ton if total_ton > 0 else np.nan
    delta_vs_target = avg_diesel_gal_ton - target_gal_ton
    extra_gal_total = max(delta_vs_target, 0) * total_ton
    impact_usd = extra_gal_total * diesel_price_per_gal

    best_day = diesel_df.loc[diesel_df["Diesel_gal_ton"].idxmin()]
    worst_day = diesel_df.loc[diesel_df["Diesel_gal_ton"].idxmax()]

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Consumo de Combustible Diésel promedio – gal/ton", f"{avg_diesel_gal_ton:,.2f}", delta=f"{delta_vs_target:+.2f} vs meta")
    k2.metric("Combustible Diésel total usado – gal", f"{total_diesel:,.2f}")
    k3.metric("Producción total analizada – ton", f"{total_ton:,.2f}")
    k4.metric("Impacto estimado por sobreconsumo", f"${impact_usd:,.2f}")

    with st.expander("⚙️ Parámetros de control", expanded=False):
        c1, c2, c3 = st.columns(3)
        c1.write(f"Meta de Consumo de Combustible Diésel: **{target_gal_ton:.2f} gal/ton**")
        c2.write(f"Tolerancia permitida: **±{tol_gal_ton:.2f} gal/ton**")
        c3.write(f"Precio de Diésel: **${diesel_price_per_gal:.4f}/gal**")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Tendencia",
        "📊 Cumplimiento",
        "🚨 Alertas",
        "💰 Impacto económico",
        "📋 Detalle diario"
    ])

    with tab1:
        fig1 = px.line(
            diesel_df,
            x="Fecha",
            y="Diesel_gal_ton",
            markers=True,
            title="Consumo de Combustible Diésel – gal/ton por día"
        )
        fig1.add_hline(y=target_gal_ton, line_dash="dash", annotation_text="Meta de operación")
        fig1.add_hline(y=target_gal_ton + tol_gal_ton, line_dash="dot", annotation_text="+ Tolerancia")
        fig1.add_hline(y=target_gal_ton - tol_gal_ton, line_dash="dot", annotation_text="- Tolerancia")
        st.plotly_chart(plot_white_layout(fig1), use_container_width=True)

        fig2 = px.line(
            diesel_df,
            x="Fecha",
            y="Consumo_Diesel_Acumulado_gal_ton",
            markers=True,
            title="Tendencia acumulada mensual del Consumo de Combustible Diésel"
        )
        st.plotly_chart(plot_white_layout(fig2), use_container_width=True)

        fig3 = px.funnel(
            diesel_flow_df,
            x="Valor",
            y="Etapa",
            title="Flujo de Combustible Diésel: P2 → Hyundai → Equipos"
        )
        st.plotly_chart(plot_white_layout(fig3, height=380), use_container_width=True)

        fig4 = px.bar(
            equipos_df,
            x="Equipo",
            y="Galones",
            title="Distribución de Combustible Diésel por equipo"
        )
        st.plotly_chart(plot_white_layout(fig4, height=320), use_container_width=True)

    with tab2:
        diesel_df["Estado"] = np.where(
            diesel_df["Diesel_gal_ton"].between(target_gal_ton - tol_gal_ton, target_gal_ton + tol_gal_ton),
            "Dentro de meta",
            "Fuera de meta"
        )

        resumen_estado = (
            diesel_df.groupby("Estado", dropna=False)
            .agg(Dias=("Fecha", "count"), Toneladas=("Toneladas", "sum"))
            .reset_index()
        )
        st.dataframe(resumen_estado, use_container_width=True, hide_index=True)

        fig = px.bar(
            diesel_df,
            x="Fecha",
            y="Diesel_gal_ton",
            color="Estado",
            title="Cumplimiento diario del Consumo de Combustible Diésel vs meta"
        )
        fig.add_hline(y=target_gal_ton, line_dash="dash", annotation_text="Meta de operación")
        st.plotly_chart(plot_white_layout(fig), use_container_width=True)

        c1, c2 = st.columns(2)
        c1.info(
            f"**Mejor día:** {best_day['Fecha'].strftime('%Y-%m-%d')}  \n"
            f"Consumo de Combustible Diésel: **{best_day['Diesel_gal_ton']:.2f} gal/ton**  \n"
            f"Producción: **{best_day['Toneladas']:.2f} ton**"
        )
        c2.error(
            f"**Peor día:** {worst_day['Fecha'].strftime('%Y-%m-%d')}  \n"
            f"Consumo de Combustible Diésel: **{worst_day['Diesel_gal_ton']:.2f} gal/ton**  \n"
            f"Producción: **{worst_day['Toneladas']:.2f} ton**"
        )

    with tab3:
        st.caption("Alertas generadas por desviaciones del Consumo de Combustible Diésel y por producción baja.")
        st.dataframe(alerts_df, use_container_width=True, hide_index=True)

        if len(alerts_df) > 0:
            for _, row in alerts_df.head(8).iterrows():
                if "🚨" in row["Nivel"]:
                    st.error(f"{row['Fecha']} · {row['Mensaje']}")
                elif "⚠️" in row["Nivel"]:
                    st.warning(f"{row['Fecha']} · {row['Mensaje']}")
                else:
                    st.info(f"{row['Fecha']} · {row['Mensaje']}")
        else:
            st.success("No se detectaron alertas relevantes en el Consumo de Combustible Diésel.")

    with tab4:
        impact_df = diesel_df.copy()
        impact_df["Delta_gal_ton"] = impact_df["Diesel_gal_ton"] - target_gal_ton
        impact_df["Exceso_Diesel_gal"] = np.where(
            impact_df["Delta_gal_ton"] > 0,
            impact_df["Delta_gal_ton"] * impact_df["Toneladas"],
            0
        )
        impact_df["Sobrecosto_USD"] = impact_df["Exceso_Diesel_gal"] * diesel_price_per_gal

        impact_table = impact_df[[
            "Fecha", "Toneladas", "Diesel_gal_ton", "Delta_gal_ton",
            "Exceso_Diesel_gal", "Sobrecosto_USD"
        ]].copy()
        impact_table["Fecha"] = impact_table["Fecha"].dt.strftime("%Y-%m-%d")
        impact_table = impact_table.rename(columns={
            "Toneladas": "Producción (ton)",
            "Diesel_gal_ton": "Consumo de Combustible Diésel – gal/ton",
            "Delta_gal_ton": "Desviación vs meta (gal/ton)",
            "Exceso_Diesel_gal": "Exceso de Diésel (gal)",
            "Sobrecosto_USD": "Sobrecosto estimado (USD)"
        })

        st.metric("Sobrecosto estimado acumulado", f"${impact_table['Sobrecosto estimado (USD)'].sum():,.2f}")

        fig = px.bar(
            impact_table,
            x="Fecha",
            y="Sobrecosto estimado (USD)",
            title="Sobrecosto estimado por desviación del Consumo de Combustible Diésel"
        )
        st.plotly_chart(plot_white_layout(fig), use_container_width=True)
        st.dataframe(impact_table, use_container_width=True, hide_index=True)

    with tab5:
        detail_df = diesel_df.copy()
        detail_df["Fecha"] = detail_df["Fecha"].dt.strftime("%Y-%m-%d")
        detail_df = detail_df.rename(columns={
            "Tipo_Mezcla": "Tipo de Mezcla",
            "Toneladas": "Producción (ton)",
            "Diesel_gal": "Combustible Diésel usado – gal",
            "Diesel_gal_ton": "Consumo de Combustible Diésel – gal/ton",
            "Consumo_Diesel_Acumulado_gal_ton": "Consumo acumulado – gal/ton"
        })
        st.dataframe(
            detail_df[[
                "Fecha", "Tipo de Mezcla", "Producción (ton)",
                "Combustible Diésel usado – gal",
                "Consumo de Combustible Diésel – gal/ton",
                "Consumo acumulado – gal/ton"
            ]],
            use_container_width=True,
            hide_index=True
        )


def render_ac30_module(
    df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    target_kg_ton: float = 52.0,
    tol_kg_ton: float = 3.0,
    ac30_price_per_kg: float = 0.6624
):
    st.subheader("🛢️ Módulo de Contenido de Asfalto (AC30)")
    st.markdown("""
    ### 🎯 Qué responde este módulo
    - ¿Estamos cumpliendo el diseño de Contenido de Asfalto (AC30)?
    - ¿Qué días hubo sobreconsumo o subconsumo?
    - ¿Cuál fue el impacto económico de las desviaciones?
    - ¿La operación está estable o presenta variabilidad?
    """)

    ac30_df = df.copy().sort_values("Fecha").reset_index(drop=True)
    ac30_df["Toneladas_Acumuladas"] = ac30_df["Toneladas"].cumsum()
    ac30_df["Asfalto_AC30_Acumulado_kg"] = ac30_df["Contenido_Asfalto_AC30_kg"].cumsum()
    ac30_df["Asfalto_AC30_Acumulado_gal"] = ac30_df["Asfalto_AC30_gal"].cumsum()
    ac30_df["Contenido_Asfalto_AC30_Acumulado_kg_ton"] = np.where(
        ac30_df["Toneladas_Acumuladas"] > 0,
        ac30_df["Asfalto_AC30_Acumulado_kg"] / ac30_df["Toneladas_Acumuladas"],
        np.nan
    )
    ac30_df["Consumo_Asfalto_AC30_Acumulado_gl_ton"] = np.where(
        ac30_df["Toneladas_Acumuladas"] > 0,
        ac30_df["Asfalto_AC30_Acumulado_gal"] / ac30_df["Toneladas_Acumuladas"],
        np.nan
    )

    alerts_df = build_ac30_alerts(ac30_df, target_kg_ton, tol_kg_ton)

    total_ton = ac30_df["Toneladas"].sum()
    total_kg = ac30_df["Contenido_Asfalto_AC30_kg"].sum()
    total_gal = ac30_df["Asfalto_AC30_gal"].sum()
    avg_kg_ton = total_kg / total_ton if total_ton > 0 else np.nan
    avg_gl_ton = total_gal / total_ton if total_ton > 0 else np.nan
    delta_vs_target = avg_kg_ton - target_kg_ton
    extra_kg_total = max(delta_vs_target, 0) * total_ton
    impact_usd = extra_kg_total * ac30_price_per_kg
    target_gl_ton = target_kg_ton / 3.861

    best_day = ac30_df.loc[ac30_df["Contenido_Asfalto_AC30_kg_ton"].idxmin()]
    worst_day = ac30_df.loc[ac30_df["Contenido_Asfalto_AC30_kg_ton"].idxmax()]

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Contenido de Asfalto (AC30) promedio – kg/ton", f"{avg_kg_ton:,.2f}", delta=f"{delta_vs_target:+.2f} vs meta")
    k2.metric("Consumo de Asfalto (AC30) promedio – gl/ton", f"{avg_gl_ton:,.2f}")
    k3.metric("Contenido total de Asfalto (AC30) usado – kg", f"{total_kg:,.2f}")
    k4.metric("Impacto estimado por sobreconsumo", f"${impact_usd:,.2f}")

    with st.expander("⚙️ Parámetros de control", expanded=False):
        c1, c2, c3 = st.columns(3)
        c1.write(f"Meta de Contenido de Asfalto (AC30): **{target_kg_ton:.2f} kg/ton**")
        c2.write(f"Tolerancia permitida: **±{tol_kg_ton:.2f} kg/ton**")
        c3.write(f"Precio de Asfalto (AC30): **${ac30_price_per_kg:.4f}/kg**")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Tendencia",
        "📊 Cumplimiento",
        "🚨 Alertas",
        "💰 Impacto económico",
        "📋 Detalle diario"
    ])

    with tab1:
        fig1 = px.line(
            ac30_df,
            x="Fecha",
            y="Contenido_Asfalto_AC30_kg_ton",
            markers=True,
            title="Contenido de Asfalto (AC30) – kg/ton por día"
        )
        fig1.add_hline(y=target_kg_ton, line_dash="dash", annotation_text="Meta de diseño")
        fig1.add_hline(y=target_kg_ton + tol_kg_ton, line_dash="dot", annotation_text="+ Tolerancia")
        fig1.add_hline(y=target_kg_ton - tol_kg_ton, line_dash="dot", annotation_text="- Tolerancia")
        st.plotly_chart(plot_white_layout(fig1), use_container_width=True)

        fig2 = px.line(
            ac30_df,
            x="Fecha",
            y="Consumo_Asfalto_AC30_gl_ton",
            markers=True,
            title="Consumo de Asfalto (AC30) – gl/ton por día"
        )
        fig2.add_hline(y=target_gl_ton, line_dash="dash", annotation_text="Meta equivalente")
        st.plotly_chart(plot_white_layout(fig2), use_container_width=True)

        fig3 = px.line(
            ac30_df,
            x="Fecha",
            y=["Contenido_Asfalto_AC30_Acumulado_kg_ton", "Consumo_Asfalto_AC30_Acumulado_gl_ton"],
            markers=True,
            title="Tendencia acumulada mensual del Contenido de Asfalto (AC30)"
        )
        st.plotly_chart(plot_white_layout(fig3), use_container_width=True)

        fig4 = px.bar(
            inventory_df,
            x="Concepto",
            y="Kg",
            title="Inventario de Asfalto (AC30): inventario, recepción, consumo y diferencia"
        )
        st.plotly_chart(plot_white_layout(fig4, height=380), use_container_width=True)

    with tab2:
        ac30_df["Estado"] = np.where(
            ac30_df["Contenido_Asfalto_AC30_kg_ton"].between(target_kg_ton - tol_kg_ton, target_kg_ton + tol_kg_ton),
            "Dentro de diseño",
            "Fuera de diseño"
        )

        resumen_estado = (
            ac30_df.groupby("Estado", dropna=False)
            .agg(Dias=("Fecha", "count"), Toneladas=("Toneladas", "sum"))
            .reset_index()
        )
        st.dataframe(resumen_estado, use_container_width=True, hide_index=True)

        fig = px.bar(
            ac30_df,
            x="Fecha",
            y="Contenido_Asfalto_AC30_kg_ton",
            color="Estado",
            title="Cumplimiento diario del Contenido de Asfalto (AC30) vs diseño"
        )
        fig.add_hline(y=target_kg_ton, line_dash="dash", annotation_text="Meta de diseño")
        st.plotly_chart(plot_white_layout(fig), use_container_width=True)

        c1, c2 = st.columns(2)
        c1.info(
            f"**Mejor día:** {best_day['Fecha'].strftime('%Y-%m-%d')}  \n"
            f"Contenido de Asfalto (AC30): **{best_day['Contenido_Asfalto_AC30_kg_ton']:.2f} kg/ton**  \n"
            f"Consumo: **{best_day['Consumo_Asfalto_AC30_gl_ton']:.2f} gl/ton**  \n"
            f"Producción: **{best_day['Toneladas']:.2f} ton**"
        )
        c2.error(
            f"**Peor día:** {worst_day['Fecha'].strftime('%Y-%m-%d')}  \n"
            f"Contenido de Asfalto (AC30): **{worst_day['Contenido_Asfalto_AC30_kg_ton']:.2f} kg/ton**  \n"
            f"Consumo: **{worst_day['Consumo_Asfalto_AC30_gl_ton']:.2f} gl/ton**  \n"
            f"Producción: **{worst_day['Toneladas']:.2f} ton**"
        )

    with tab3:
        st.caption("Alertas generadas por desviaciones del Contenido de Asfalto (AC30) y por producción baja.")
        st.dataframe(alerts_df, use_container_width=True, hide_index=True)

        if len(alerts_df) > 0:
            for _, row in alerts_df.head(8).iterrows():
                if "🚨" in row["Nivel"]:
                    st.error(f"{row['Fecha']} · {row['Mensaje']}")
                elif "⚠️" in row["Nivel"]:
                    st.warning(f"{row['Fecha']} · {row['Mensaje']}")
                else:
                    st.info(f"{row['Fecha']} · {row['Mensaje']}")
        else:
            st.success("No se detectaron alertas relevantes en el Contenido de Asfalto (AC30).")

    with tab4:
        impact_df = ac30_df.copy()
        impact_df["Delta_kg_ton"] = impact_df["Contenido_Asfalto_AC30_kg_ton"] - target_kg_ton
        impact_df["Exceso_Asfalto_kg"] = np.where(
            impact_df["Delta_kg_ton"] > 0,
            impact_df["Delta_kg_ton"] * impact_df["Toneladas"],
            0
        )
        impact_df["Sobrecosto_USD"] = impact_df["Exceso_Asfalto_kg"] * ac30_price_per_kg

        impact_table = impact_df[[
            "Fecha", "Toneladas", "Contenido_Asfalto_AC30_kg_ton",
            "Delta_kg_ton", "Exceso_Asfalto_kg", "Sobrecosto_USD"
        ]].copy()
        impact_table["Fecha"] = impact_table["Fecha"].dt.strftime("%Y-%m-%d")
        impact_table = impact_table.rename(columns={
            "Toneladas": "Producción (ton)",
            "Contenido_Asfalto_AC30_kg_ton": "Contenido de Asfalto (AC30) – kg/ton",
            "Delta_kg_ton": "Desviación vs meta (kg/ton)",
            "Exceso_Asfalto_kg": "Exceso de Asfalto (kg)",
            "Sobrecosto_USD": "Sobrecosto estimado (USD)"
        })

        st.metric("Sobrecosto estimado acumulado", f"${impact_table['Sobrecosto estimado (USD)'].sum():,.2f}")

        fig = px.bar(
            impact_table,
            x="Fecha",
            y="Sobrecosto estimado (USD)",
            title="Sobrecosto estimado por desviación del Contenido de Asfalto (AC30)"
        )
        st.plotly_chart(plot_white_layout(fig), use_container_width=True)
        st.dataframe(impact_table, use_container_width=True, hide_index=True)

    with tab5:
        detail_df = ac30_df.copy()
        detail_df["Fecha"] = detail_df["Fecha"].dt.strftime("%Y-%m-%d")
        detail_df = detail_df.rename(columns={
            "Tipo_Mezcla": "Tipo de Mezcla",
            "Toneladas": "Producción (ton)",
            "Asfalto_AC30_gal": "Asfalto (AC30) usado – gal",
            "Contenido_Asfalto_AC30_kg": "Asfalto (AC30) usado – kg",
            "Consumo_Asfalto_AC30_gl_ton": "Consumo de Asfalto (AC30) – gl/ton",
            "Contenido_Asfalto_AC30_kg_ton": "Contenido de Asfalto (AC30) – kg/ton",
            "Consumo_Asfalto_AC30_Acumulado_gl_ton": "Consumo acumulado – gl/ton",
            "Contenido_Asfalto_AC30_Acumulado_kg_ton": "Contenido acumulado – kg/ton"
        })
        st.dataframe(
            detail_df[[
                "Fecha", "Tipo de Mezcla", "Producción (ton)",
                "Asfalto (AC30) usado – gal", "Asfalto (AC30) usado – kg",
                "Consumo de Asfalto (AC30) – gl/ton",
                "Contenido de Asfalto (AC30) – kg/ton",
                "Consumo acumulado – gl/ton",
                "Contenido acumulado – kg/ton"
            ]],
            use_container_width=True,
            hide_index=True
        )


# =========================
# HEADER
# =========================
st.markdown('<div class="sas-title">SAS SmartPlant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sas-sub">Control inteligente de combustible diésel, contenido de asfalto (AC30), producción, calidad y alertas en tiempo real</div>',
    unsafe_allow_html=True
)


# =========================
# KPI TOP
# =========================
total_ton = prod_history["Toneladas"].sum()
total_diesel = prod_history["Diesel_gal"].sum()
total_ac30 = prod_history["Contenido_Asfalto_AC30_kg"].sum()
avg_diesel_gal_ton = total_diesel / total_ton
avg_ac30_kg_ton = total_ac30 / total_ton

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Producción analizada", f"{total_ton:,.0f} ton")
col2.metric("Combustible Diésel usado", f"{total_diesel:,.0f} gal")
col3.metric("Asfalto (AC30) usado", f"{total_ac30:,.0f} kg")
col4.metric("Consumo Diésel – gal/ton", f"{avg_diesel_gal_ton:,.2f}")
col5.metric("Contenido Asfalto – kg/ton", f"{avg_ac30_kg_ton:,.2f}")

st.divider()


# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Resumen Ejecutivo",
    "Combustible Diésel",
    "Contenido de Asfalto (AC30)",
    "Producción",
    "Calidad",
    "Alertas Inteligentes"
])


# =========================
# TAB 1 - RESUMEN
# =========================
with tab1:
    left, right = st.columns([1.6, 1])

    with left:
        st.subheader("Resumen ejecutivo")
        render_resumen_operacional(prod_history)

    with right:
        st.subheader("Estado operativo")

        render_html_alert(
            "<b>Alerta roja:</b> Existe una diferencia de 300 gal entre el despacho a Hyundai y la distribución a equipos.",
            "red"
        )
        render_html_alert(
            "<b>Alerta amarilla:</b> El Consumo de Combustible Diésel supera la meta operativa en varios días del período.",
            "yellow"
        )
        render_html_alert(
            "<b>Alerta amarilla:</b> El Contenido de Asfalto (AC30) presenta variabilidad y días fuera de diseño.",
            "yellow"
        )
        render_html_alert(
            "<b>Producción:</b> La mezcla IV-B domina la operación analizada.",
            "green"
        )

        st.subheader("Insight automático")
        st.info(
            "El sistema detecta que la operación presenta dos focos principales de decisión: "
            "eficiencia del Combustible Diésel por tonelada y cumplimiento del Contenido de Asfalto (AC30) vs diseño."
        )


# =========================
# TAB 2 - DIÉSEL
# =========================
with tab2:
    render_diesel_module(
        df=prod_history,
        diesel_flow_df=diesel_flow,
        equipos_df=equipos,
        target_gal_ton=1.80,
        tol_gal_ton=0.25,
        diesel_price_per_gal=4.30
    )


# =========================
# TAB 3 - AC30
# =========================
with tab3:
    render_ac30_module(
        df=prod_history,
        inventory_df=ac30_inventory,
        target_kg_ton=52.0,
        tol_kg_ton=3.0,
        ac30_price_per_kg=0.6624
    )


# =========================
# TAB 4 - PRODUCCIÓN
# =========================
with tab4:
    c1, c2 = st.columns([1.2, 1])

    with c1:
        st.subheader("Producción")
        fig = px.bar(
            prod_history,
            x="Fecha",
            y="Toneladas",
            color="Tipo_Mezcla",
            title="Producción diaria por tipo de mezcla"
        )
        st.plotly_chart(plot_white_layout(fig, height=360), use_container_width=True)

        fig_mix = px.pie(
            mezclas,
            names="Tipo de mezcla",
            values="Toneladas",
            title="Participación por tipo de mezcla"
        )
        st.plotly_chart(plot_white_layout(fig_mix, height=360), use_container_width=True)

    with c2:
        st.subheader("Resumen de producción")
        st.metric("Producción total", f"{total_ton:,.2f} ton")
        st.metric("Mezcla dominante", "IV-B")
        st.metric("Promedio diario", f"{prod_history['Toneladas'].mean():,.2f} ton")
        st.metric("Días analizados", f"{len(prod_history)}")
        st.write("**Interpretación**")
        st.write("- La producción analizada se concentra en mezcla IV-B.")
        st.write("- Los días de baja producción pueden distorsionar indicadores por tonelada.")
        st.write("- Conviene analizar producción, diésel y contenido de asfalto en conjunto.")
        st.info("Se recomienda comparar eficiencia y cumplimiento por mezcla: IV-B vs MS-22.")


# =========================
# TAB 5 - CALIDAD
# =========================
with tab5:
    c1, c2 = st.columns([1.1, 1])

    with c1:
        st.subheader("Control de calidad")
        st.dataframe(calidad_data, use_container_width=True, hide_index=True)

    with c2:
        st.subheader("Comparación contra diseño")
        render_html_alert(
            "<b>Desviación:</b> Se detectan variaciones en contenido de asfalto y vacíos.",
            "yellow"
        )
        render_html_alert(
            "<b>No cumplimiento:</b> La estabilidad no cumple con el diseño esperado.",
            "red"
        )
        render_html_alert(
            "<b>Acción sugerida:</b> Ajustar mezcla y validar muestreo antes del siguiente lote.",
            "green"
        )


# =========================
# TAB 6 - ALERTAS
# =========================
with tab6:
    st.subheader("Alertas inteligentes")

    diesel_alerts = build_diesel_alerts(prod_history, target_gal_ton=1.80, tol_gal_ton=0.25)
    ac30_alerts = build_ac30_alerts(prod_history, target_kg_ton=52.0, tol_kg_ton=3.0)

    render_html_alert(
        "<b>1. Desbalance de Combustible Diésel</b><br>La distribución a equipos no cuadra completamente con el despacho a Hyundai.",
        "red"
    )
    render_html_alert(
        "<b>2. Sobreconsumo de Combustible Diésel</b><br>Se detectan días por encima de la meta operativa de gal/ton.",
        "yellow"
    )
    render_html_alert(
        "<b>3. Desviación de Contenido de Asfalto (AC30)</b><br>Se detectan días fuera del rango de diseño.",
        "red"
    )
    render_html_alert(
        "<b>4. Riesgo de interpretación por baja producción</b><br>Hay días con tonelaje bajo que requieren análisis cuidadoso.",
        "yellow"
    )

    st.subheader("Resumen consolidado de alertas")
    all_alerts = pd.concat([diesel_alerts, ac30_alerts], ignore_index=True)
    if not all_alerts.empty:
        st.dataframe(all_alerts, use_container_width=True, hide_index=True)
    else:
        st.success("No se detectaron alertas consolidadas en el período analizado.")

    st.subheader("Acciones sugeridas por SAS SmartPlant")
    st.write("1. Revisar la conciliación física entre Recepción P2, despacho a Hyundai y distribución final.")
    st.write("2. Controlar días con sobreconsumo de Combustible Diésel y revisar tiempos muertos.")
    st.write("3. Validar el Contenido de Asfalto (AC30) contra diseño por tipo de mezcla.")
    st.write("4. Separar análisis por mezcla IV-B y MS-22 para evitar conclusiones mezcladas.")
    st.write("5. Priorizar días de alta producción para evaluar desempeño real de la operación.")

st.divider()
st.caption("SAS SmartPlant • Demo para inversionistas")
