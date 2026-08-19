import streamlit as st

st.set_page_config(page_title="Home | Cricbuzz LiveStats", page_icon="🏠", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .hero-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .hero-title { font-size: 2.2rem; font-weight: 800; color: #38bdf8; }
    .hero-desc { font-size: 1.05rem; color: #cbd5e1; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-card">
        <div class="hero-title"> Welcome to Cricbuzz LiveStats</div>
        <div class="hero-desc">
            An enterprise-grade cricket analytics portal designed for real-time match tracking, 
            deep SQL querying, player statistics visualization, and administrative data operations.
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.markdown("###  Platform Capabilities")
        st.markdown("""
        * **Live Scores**: Integrated REST API feeds for active international & league matches.
        * **SQL Engine**: 25 pre-configured relational queries covering complex aggregations and joins.
        * **Visualizations**: Interactive Plotly charts for ICC player ratings and rankings.
        * **Database Admin**: Full CRUD capabilities with state management for dynamic updates.
        """)

with col2:
    with st.container(border=True):
        st.markdown("### 🛠 Architecture Overview")
        st.markdown("""
        * **Frontend**: Streamlit Multi-Page Layout with custom CSS design tokens.
        * **Database**: SQLite database normalized to **3NF**.
        * **Data Processing**: Pandas DataFrames & NumPy matrix processing.
        * **Visual Analytics**: Dynamic Plotly Express rendering engine.
        """)