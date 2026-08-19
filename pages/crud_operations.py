import streamlit as st
import pandas as pd
from utils.db_connection import execute_query, execute_commit

st.set_page_config(page_title="CRUD Operations | Cricbuzz LiveStats", page_icon="🛠️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ Player Roster CRUD Operations")
st.caption("Admin portal for creating, reading, updating, and removing database entries")
st.divider()

# Toast Notification System
if "toast_msg" in st.session_state:
    st.success(st.session_state["toast_msg"])
    del st.session_state["toast_msg"]

tab_read, tab_create, tab_update, tab_delete = st.tabs([
    "📖 Read / View Records", 
    "➕ Create New Player", 
    "✏️ Update Existing Player", 
    "🗑️ Delete Player"
])

with tab_read:
    with st.container(border=True):
        st.subheader("Active Player Database Roster")
        df = execute_query("""
            SELECT p.player_id, p.full_name, t.team_name, p.playing_role, p.batting_style, p.bowling_style 
            FROM players p 
            LEFT JOIN teams t ON p.team_id = t.team_id 
            ORDER BY p.player_id DESC;
        """)
        st.dataframe(df, use_container_width=True, hide_index=True)

with tab_create:
    with st.container(border=True):
        st.subheader("Insert New Player Profile")
        with st.form("add_player_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("Full Name")
                role = st.selectbox("Playing Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
                bat_style = st.text_input("Batting Style", value="Right-hand bat")
            with col2:
                team_id = st.number_input("Team ID (1: IND, 2: AUS, 3: ENG, 4: SA)", min_value=1, value=1)
                bowl_style = st.text_input("Bowling Style", value="Right-arm fast")
            
            submitted = st.form_submit_button("Submit Record", type="primary", use_container_width=True)
            if submitted:
                if full_name:
                    sql = "INSERT INTO players (full_name, team_id, playing_role, batting_style, bowling_style) VALUES (?, ?, ?, ?, ?)"
                    new_id = execute_commit(sql, (full_name, team_id, role, bat_style, bowl_style))
                    st.session_state["toast_msg"] = f"Player '{full_name}' created successfully with ID #{new_id}!"
                    st.rerun()
                else:
                    st.error("Please provide a valid player name.")

with tab_update:
    with st.container(border=True):
        st.subheader("Modify Player Details")
        with st.form("update_player_form"):
            col1, col2 = st.columns(2)
            with col1:
                player_id = st.number_input("Target Player ID", min_value=1, step=1)
            with col2:
                new_role = st.selectbox("Updated Playing Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
            
            submitted_update = st.form_submit_button("Update Player Role", use_container_width=True)
            if submitted_update:
                sql = "UPDATE players SET playing_role = ? WHERE player_id = ?"
                execute_commit(sql, (new_role, player_id))
                st.session_state["toast_msg"] = f"Updated Player #{player_id} role to '{new_role}'."
                st.rerun()

with tab_delete:
    with st.container(border=True):
        st.subheader("Remove Player from Database")
        with st.form("delete_player_form"):
            p_id = st.number_input("Player ID to Delete", min_value=1, step=1)
            submitted_delete = st.form_submit_button("Delete Player Record", type="primary", use_container_width=True)
            if submitted_delete:
                execute_commit("DELETE FROM player_stats WHERE player_id = ?", (p_id,))
                execute_commit("DELETE FROM players WHERE player_id = ?", (p_id,))
                st.session_state["toast_msg"] = f"Player #{p_id} removed from database."
                st.rerun()