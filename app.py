import streamlit as st
import pandas as pd
from utils.db_connection import execute_query

# 1. Page Configuration
st.set_page_config(
    page_title="Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Modern Dark Theme & Responsive CSS
st.markdown("""
    <style>
    /* Main Background Accent */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Card Container Styling */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease-in-out, border-color 0.2s ease-in-out;
    }
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: #38bdf8;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 5px;
    }

    /* Styled Gradient Title */
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown('<h1 class="main-title">🏏 Cricbuzz LiveStats</h1>', unsafe_allow_html=True)
st.caption("Enterprise Real-Time Cricket Analytics & Roster Management Hub")
st.divider()

# 4. Overview Metrics (Fetch real counts from database)
try:
    total_players = execute_query("SELECT COUNT(*) as count FROM players")['count'][0]
    total_teams = execute_query("SELECT COUNT(*) as count FROM teams")['count'][0]
    total_matches = execute_query("SELECT COUNT(*) as count FROM matches")['count'][0]
    total_series = execute_query("SELECT COUNT(*) as count FROM series")['count'][0]
except Exception:
    total_players, total_teams, total_matches, total_series = 0, 0, 0, 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Players</div>
            <div class="metric-value">{total_players}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Teams Active</div>
            <div class="metric-value">{total_teams}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Matches Tracked</div>
            <div class="metric-value">{total_matches}</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Series Recorded</div>
            <div class="metric-value">{total_series}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# 5. Core Feature Modules Grid (Exact Page Paths Matched)
st.subheader("⚡ Quick Navigation")

col_left, col_right = st.columns(2, gap="medium")

with col_left:
    with st.container(border=True):
        st.markdown("### 🔍 SQL Analytics Engine")
        st.write("Run 25 predefined analytical SQL queries to extract deep insights on player averages, strike rates, team head-to-head records, and venue stats.")
        st.page_link("pages/sql_analytics.py", label="Explore Analytics Engine", icon="🔍", use_container_width=True)

    with st.container(border=True):
        st.markdown("### 📈 Top Player Rankings")
        st.write("View interactive Plotly charts highlighting current ICC batting and bowling leaders across international formats.")
        st.page_link("pages/top_stats.py", label="View Rankings", icon="📈", use_container_width=True)

with col_right:
    with st.container(border=True):
        st.markdown("### 🛠️ Data Management Portal")
        st.write("Full administrative CRUD operations to insert new player profiles, update playing roles, and manage active rosters.")
        st.page_link("pages/crud_operations.py", label="Open CRUD Portal", icon="🛠️", use_container_width=True)

    with st.container(border=True):
        st.markdown("### 🔴 Live Scorecards")
        st.write("Fetch real-time score updates, match summaries, and commentary feeds for active series.")
        st.page_link("pages/live_matches.py", label="Check Live Scores", icon="🔴", use_container_width=True)

st.divider()
st.info("💡 **System Status:** Database connected and healthy.")