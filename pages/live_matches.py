import streamlit as st
import pandas as pd
from utils.api_handler import fetch_top_players

st.set_page_config(page_title="Live Matches | Cricbuzz LiveStats", page_icon="🔴", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .status-badge {
        background-color: #ef4444;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 10px;
    }
    .match-card {
        background: #1e293b;
        border-left: 4px solid #ef4444;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔴 Live Cricket Scorecards & Feeds")
st.caption("Real-time match updates and live performance feeds")
st.divider()

st.markdown('<span class="status-badge">LIVE UPDATES ACTIVE</span>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("🏏 Match 1: IND vs AUS")
        st.caption("Border-Gavaskar Trophy • 3rd Test • Day 4")
        st.markdown("**India:** 342/8 (90.0 ov)")
        st.markdown("**Australia:** 215 & 180/4 (52.3 ov)")
        st.info("Australia need 145 runs to win.")

with col2:
    with st.container(border=True):
        st.subheader("🏏 Match 2: ENG vs SA")
        st.caption("International Series • 2nd ODI")
        st.markdown("**England:** 288/6 (50.0 ov)")
        st.markdown("**South Africa:** 192/3 (32.0 ov)")
        st.success("South Africa need 97 runs in 18.0 overs.")