import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api_handler import fetch_top_players

st.set_page_config(page_title="Top Stats | Cricbuzz LiveStats", page_icon="📈", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    </style>
""", unsafe_allow_html=True)

st.title("📈 ICC Player Rankings & Visualizations")
st.caption("Interactive Plotly analytics for top ICC performers")
st.divider()

data = fetch_top_players()

tab1, tab2 = st.tabs(["🏏 Batting Rankings", "🎳 Bowling Rankings"])

# Helper function for chart styling
def style_plotly_chart(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#e2e8f0"),
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#334155")
    )
    return fig

with tab1:
    col_table, col_chart = st.columns([1, 1.2], gap="medium")
    df_bat = pd.DataFrame(data["batting"])
    
    with col_table:
        with st.container(border=True):
            st.subheader("Batting Leaders Table")
            st.dataframe(df_bat, use_container_width=True, hide_index=True)
            
    with col_chart:
        with st.container(border=True):
            st.subheader("Rating Comparison")
            fig_bat = px.bar(df_bat, x="player", y="rating", color="team", 
                             color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(style_plotly_chart(fig_bat), use_container_width=True)

with tab2:
    col_table_b, col_chart_b = st.columns([1, 1.2], gap="medium")
    df_bowl = pd.DataFrame(data["bowling"])
    
    with col_table_b:
        with st.container(border=True):
            st.subheader("Bowling Leaders Table")
            st.dataframe(df_bowl, use_container_width=True, hide_index=True)
            
    with col_chart_b:
        with st.container(border=True):
            st.subheader("Rating Comparison")
            fig_bowl = px.bar(df_bowl, x="player", y="rating", color="team", 
                              color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(style_plotly_chart(fig_bowl), use_container_width=True)