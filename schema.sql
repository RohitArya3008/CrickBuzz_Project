-- Schema DDL
CREATE TABLE IF NOT EXISTS venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    capacity INTEGER
);

CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    team_id INTEGER,
    playing_role TEXT,
    batting_style TEXT,
    bowling_style TEXT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS series (
    series_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_name TEXT NOT NULL,
    host_country TEXT,
    match_type TEXT,
    start_date DATE,
    total_matches INTEGER
);

CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id INTEGER,
    match_description TEXT,
    team1_id INTEGER,
    team2_id INTEGER,
    venue_id INTEGER,
    match_date DATE,
    winning_team_id INTEGER,
    toss_winner_id INTEGER,
    toss_decision TEXT,
    victory_margin INTEGER,
    victory_type TEXT,
    FOREIGN KEY (series_id) REFERENCES series(series_id),
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id),
    FOREIGN KEY (winning_team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS player_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    format TEXT,
    matches_played INTEGER DEFAULT 0,
    runs_scored INTEGER DEFAULT 0,
    batting_average REAL DEFAULT 0.0,
    strike_rate REAL DEFAULT 0.0,
    centuries INTEGER DEFAULT 0,
    wickets_taken INTEGER DEFAULT 0,
    bowling_average REAL DEFAULT 0.0,
    economy_rate REAL DEFAULT 0.0,
    catches INTEGER DEFAULT 0,
    stumpings INTEGER DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

CREATE TABLE IF NOT EXISTS batting_performances (
    perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    innings INTEGER,
    batting_position INTEGER,
    runs_scored INTEGER,
    balls_faced INTEGER,
    year INTEGER,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

-- Seed Initial Sample Data
INSERT INTO teams (team_name, country) VALUES 
('India', 'India'),
('Australia', 'Australia'),
('England', 'England'),
('South Africa', 'South Africa');

INSERT INTO venues (venue_name, city, country, capacity) VALUES 
('Wankhede Stadium', 'Mumbai', 'India', 33000),
('Narendra Modi Stadium', 'Ahmedabad', 'India', 132000),
('Eden Gardens', 'Kolkata', 'India', 68000),
('Melbourne Cricket Ground', 'Melbourne', 'Australia', 100024);

INSERT INTO players (full_name, team_id, playing_role, batting_style, bowling_style) VALUES 
('Virat Kohli', 1, 'Batsman', 'Right-hand bat', 'Right-arm medium'),
('Rohit Sharma', 1, 'Batsman', 'Right-hand bat', 'Right-arm offbreak'),
('Jasprit Bumrah', 1, 'Bowler', 'Right-hand bat', 'Right-arm fast'),
('Hardik Pandya', 1, 'All-rounder', 'Right-hand bat', 'Right-arm medium-fast'),
('Steve Smith', 2, 'Batsman', 'Right-hand bat', 'Right-arm legbreak'),
('Pat Cummins', 2, 'Bowler', 'Right-hand bat', 'Right-arm fast');

INSERT INTO player_stats (player_id, format, matches_played, runs_scored, batting_average, strike_rate, centuries, wickets_taken, bowling_average, economy_rate, catches, stumpings) VALUES 
(1, 'ODI', 292, 13848, 58.67, 93.58, 50, 4, 166.25, 6.21, 150, 0),
(1, 'Test', 113, 8848, 49.15, 55.56, 29, 0, 0.0, 0.0, 110, 0),
(1, 'T20I', 125, 4188, 48.69, 137.04, 1, 1, 51.0, 8.15, 50, 0),
(2, 'ODI', 262, 10709, 49.12, 92.44, 31, 8, 64.3, 5.21, 95, 0),
(3, 'ODI', 89, 85, 8.50, 45.12, 0, 149, 23.55, 4.59, 15, 0),
(4, 'ODI', 86, 1769, 34.01, 110.22, 0, 84, 35.60, 5.58, 30, 0),
(5, 'Test', 105, 9685, 56.97, 53.50, 32, 19, 52.1, 3.45, 180, 0);

INSERT INTO series (series_name, host_country, match_type, start_date, total_matches) VALUES 
('Border-Gavaskar Trophy 2024', 'Australia', 'Test', '2024-11-22', 5),
('India vs England ODI Series 2024', 'India', 'ODI', '2024-01-25', 5);

INSERT INTO matches (series_id, match_description, team1_id, team2_id, venue_id, match_date, winning_team_id, toss_winner_id, toss_decision, victory_margin, victory_type) VALUES 
(1, '1st Test - IND vs AUS', 1, 2, 4, '2024-11-22', 1, 1, 'bat', 295, 'runs'),
(2, '1st ODI - IND vs ENG', 1, 3, 2, '2024-01-25', 1, 1, 'bowl', 4, 'wickets');

INSERT INTO batting_performances (match_id, player_id, innings, batting_position, runs_scored, balls_faced, year) VALUES 
(1, 1, 2, 3, 100, 143, 2024),
(1, 2, 1, 1, 52, 60, 2024),
(2, 1, 2, 3, 85, 78, 2024);
