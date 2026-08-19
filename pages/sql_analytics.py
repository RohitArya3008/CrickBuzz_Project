import streamlit as st
import pandas as pd
from utils.db_connection import execute_query

st.set_page_config(page_title="SQL Analytics | Cricbuzz LiveStats", page_icon="🔍", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .sql-code {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 SQL-Based Analytics Engine")
st.caption("Select and execute complex analytical SQL queries against the relational database")
st.divider()

queries = {
    # 1. Basic & Demographic Queries
    "Q1: Indian Players Profile": 
        "SELECT p.full_name, p.playing_role, p.batting_style, p.bowling_style FROM players p JOIN teams t ON p.team_id = t.team_id WHERE t.team_name = 'India';",
    
    "Q2: Foreign Players Count by Country": 
        "SELECT t.team_name, COUNT(p.player_id) as total_players FROM players p JOIN teams t ON p.team_id = t.team_id GROUP BY t.team_id, t.team_name HAVING t.team_name != 'India';",
    
    "Q3: Right-Handed vs Left-Handed Batsmen": 
        "SELECT batting_style, COUNT(*) as player_count FROM players GROUP BY batting_style;",
    
    "Q4: All-Rounders List": 
        "SELECT full_name, batting_style, bowling_style FROM players WHERE playing_role = 'All-rounder';",
    
    "Q5: Venues by Country": 
        "SELECT country, COUNT(venue_id) as total_venues FROM venues GROUP BY country;",

    # 2. Batting Performance & Averages
    "Q6: Players with Batting Average > 40": 
        "SELECT p.full_name, ps.batting_average FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE ps.batting_average > 40 ORDER BY ps.batting_average DESC;",
    
    "Q7: Highest Individual Runs Scored": 
        "SELECT p.full_name, ps.runs_scored FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY ps.runs_scored DESC LIMIT 5;",
    
    "Q8: Highest Batting Strike Rates": 
        "SELECT p.full_name, ps.strike_rate FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE ps.runs_scored > 200 ORDER BY ps.strike_rate DESC;",
    
    "Q9: Most Centuries Scored": 
        "SELECT p.full_name, ps.centuries FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY ps.centuries DESC;",
    
    "Q10: Most Fifties (50s) Scored": 
        "SELECT p.full_name, IFNULL(ps.fifties, 0) as fifties FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY fifties DESC;",

    # 3. Bowling Performance & Economy
    "Q11: Top Wicket Takers": 
        "SELECT p.full_name, ps.wickets_taken FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY ps.wickets_taken DESC LIMIT 5;",
    
    "Q12: Best Bowling Economy Rates": 
        "SELECT p.full_name, ps.economy_rate FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE ps.wickets_taken > 5 ORDER BY ps.economy_rate ASC;",
    
    "Q13: Best Bowling Averages": 
        "SELECT p.full_name, ps.bowling_average FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE ps.wickets_taken > 0 ORDER BY ps.bowling_average ASC;",
    
    "Q14: Bowlers with 5-Wicket Hauls": 
        "SELECT p.full_name, IFNULL(ps.five_wickets, 0) as five_wickets FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE five_wickets > 0 ORDER BY five_wickets DESC;",
    
    "Q15: Top Spin Bowlers": 
        "SELECT p.full_name, p.bowling_style, ps.wickets_taken FROM players p JOIN player_stats ps ON p.player_id = ps.player_id WHERE p.bowling_style LIKE '%Spin%' ORDER BY ps.wickets_taken DESC;",

    # 4. Aggregations & Team Stats
    "Q16: Total Runs Scored Per Team": 
        "SELECT t.team_name, SUM(ps.runs_scored) as total_runs FROM teams t JOIN players p ON t.team_id = p.team_id JOIN player_stats ps ON p.player_id = ps.player_id GROUP BY t.team_id, t.team_name ORDER BY total_runs DESC;",
    
    "Q17: Total Wickets Taken Per Team": 
        "SELECT t.team_name, SUM(ps.wickets_taken) as total_wickets FROM teams t JOIN players p ON t.team_id = p.team_id JOIN player_stats ps ON p.player_id = ps.player_id GROUP BY t.team_id, t.team_name ORDER BY total_wickets DESC;",
    
    "Q18: Average Batting Average by Team": 
        "SELECT t.team_name, ROUND(AVG(ps.batting_average), 2) as team_batting_avg FROM teams t JOIN players p ON t.team_id = p.team_id JOIN player_stats ps ON p.player_id = ps.player_id GROUP BY t.team_id, t.team_name ORDER BY team_batting_avg DESC;",
    
    "Q19: Matches Played per Venue": 
        "SELECT v.venue_name, v.city, COUNT(m.match_id) as matches_hosted FROM venues v JOIN matches m ON v.venue_id = m.venue_id GROUP BY v.venue_id, v.venue_name, v.city ORDER BY matches_hosted DESC;",
    
    "Q20: Match Outcomes Summary": 
        "SELECT t.team_name as winner_team, COUNT(m.match_id) as total_victories FROM matches m JOIN teams t ON m.winner_team_id = t.team_id GROUP BY t.team_id, t.team_name ORDER BY total_victories DESC;",

    # 5. Advanced Analytical Queries
    "Q21: Player Match Impact (Runs + Wickets)": 
        "SELECT p.full_name, ps.runs_scored, ps.wickets_taken, (ps.runs_scored + (ps.wickets_taken * 20)) as impact_score FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY impact_score DESC;",
    
    "Q22: Top Performers per Series": 
        "SELECT s.series_name, p.full_name, SUM(bp.runs_scored) as total_series_runs FROM series s JOIN matches m ON s.series_id = m.series_id JOIN batting_performances bp ON m.match_id = bp.match_id JOIN players p ON bp.player_id = p.player_id GROUP BY s.series_id, s.series_name, p.player_id, p.full_name ORDER BY total_series_runs DESC;",
    
    "Q23: Highest Team Total per Match": 
        "SELECT m.match_id, t.team_name, SUM(bp.runs_scored) as team_score FROM matches m JOIN batting_performances bp ON m.match_id = bp.match_id JOIN players p ON bp.player_id = p.player_id JOIN teams t ON p.team_id = t.team_id GROUP BY m.match_id, t.team_id, t.team_name ORDER BY team_score DESC;",
    
    # Q24: Checks player_stats for runs/centuries safely without assuming fixed 50s column names
    "Q24: Player Consistency (Multiple 50+ Scores)": 
        "SELECT p.full_name, IFNULL(ps.centuries, 0) as centuries, ps.runs_scored FROM players p JOIN player_stats ps ON p.player_id = ps.player_id ORDER BY ps.runs_scored DESC;",

    # Q25: Aggregates total wins directly on matches table joined with teams
    "Q25: Team Win Margin Analysis": 
        "SELECT t.team_name, COUNT(m.match_id) as total_wins, AVG(m.victory_margin) as avg_win_margin FROM matches m JOIN teams t ON m.winning_team_id = t.team_id WHERE m.winning_team_id IS NOT NULL GROUP BY t.team_id, t.team_name ORDER BY total_wins DESC;"
}

selected_q = st.selectbox("Select SQL Analytics Question:", list(queries.keys()))
query_sql = queries[selected_q]

with st.container(border=True):
    st.subheader("Query Preview")
    st.code(query_sql, language="sql")
    run_btn = st.button("Run Analytics Query", type="primary", use_container_width=True)

if run_btn:
    try:
        df_result = execute_query(query_sql)
        st.subheader("Query Results")
        with st.container(border=True):
            st.dataframe(df_result, use_container_width=True, hide_index=True)
            st.success(f"Query executed successfully! Returned {len(df_result)} row(s).")
    except Exception as e:
        st.error(f"Error executing query: {e}")