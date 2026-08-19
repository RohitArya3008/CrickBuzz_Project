import requests

def fetch_live_matches():
    """
    Mocked/Fallback or live HTTP endpoint client for match data.
    Replace API_KEY with actual Cricbuzz API credentials if active.
    """
    try:
        # Mock structured response matching Cricbuzz REST API schema
        return [
            {
                "match_id": "101",
                "series": "India tour of Australia 2026",
                "match_desc": "2nd Test",
                "team1": "IND",
                "team2": "AUS",
                "score1": "312/5 (88.0 ov)",
                "score2": "Yet to bat",
                "status": "IND chose to bat",
                "venue": "MCG, Melbourne"
            },
            {
                "match_id": "102",
                "series": "IPL 2026",
                "match_desc": "Match 15",
                "team1": "CSK",
                "team2": "RCB",
                "score1": "185/6 (20.0 ov)",
                "score2": "180/8 (20.0 ov)",
                "status": "CSK won by 5 runs",
                "venue": "M. A. Chidambaram Stadium, Chennai"
            }
        ]
    except Exception as e:
        return []

def fetch_top_players():
    """Fetches top batting and bowling rankings."""
    return {
        "batting": [
            {"rank": 1, "player": "Suryakumar Yadav", "team": "IND", "rating": 861},
            {"rank": 2, "player": "Phil Salt", "team": "ENG", "rating": 802},
            {"rank": 3, "player": "Mohammad Rizwan", "team": "PAK", "rating": 781}
        ],
        "bowling": [
            {"rank": 1, "player": "Adil Rashid", "team": "ENG", "rating": 726},
            {"rank": 2, "player": "Anrich Nortje", "team": "SA", "rating": 712},
            {"rank": 3, "player": "Rashid Khan", "team": "AFG", "rating": 708}
        ]
    }