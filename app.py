import os
import json
import logging
from flask import Flask, render_template, request, jsonify
from utils.data_processor import DataProcessor
from utils.predictor import MatchPredictor

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "ipl-predictor-secret")

# Load and process data
try:
    data_processor = DataProcessor('attached_assets/matches.csv')
    predictor = MatchPredictor(data_processor)
    teams = data_processor.get_teams()
    venues = data_processor.get_venues()
    logger.info(f"Loaded {len(teams)} teams and {len(venues)} venues successfully")
except Exception as e:
    logger.error(f"Error initializing data: {e}")
    data_processor = None
    predictor = None
    teams = []
    venues = []

@app.route('/')
def index():
    """Render the home page with overall IPL statistics."""
    if not data_processor:
        return render_template('index.html', error="Failed to load data", teams=[], stats={})
    
    overall_stats = data_processor.get_overall_stats()
    return render_template('index.html', teams=teams, stats=overall_stats)

@app.route('/team-analysis')
def team_analysis():
    """Render the team analysis page."""
    if not data_processor:
        return render_template('team_analysis.html', error="Failed to load data", teams=[])
    
    selected_team = request.args.get('team', teams[0] if teams else '')
    team_stats = data_processor.get_team_stats(selected_team)
    head_to_head = data_processor.get_head_to_head(selected_team)
    return render_template('team_analysis.html', teams=teams, selected_team=selected_team, 
                          team_stats=team_stats, head_to_head=head_to_head)

@app.route('/venue-stats')
def venue_stats():
    """Render the venue statistics page."""
    if not data_processor:
        return render_template('venue_stats.html', error="Failed to load data", venues=[])
    
    selected_venue = request.args.get('venue', venues[0] if venues else '')
    venue_stats = data_processor.get_venue_stats(selected_venue)
    return render_template('venue_stats.html', venues=venues, selected_venue=selected_venue, 
                          venue_stats=venue_stats)

@app.route('/predict')
def predict():
    """Render the prediction page."""
    if not data_processor:
        return render_template('predict.html', error="Failed to load data", teams=[], venues=[])
    
    return render_template('predict.html', teams=teams, venues=venues)

@app.route('/api/predict', methods=['POST'])
def predict_match():
    """API endpoint for match prediction."""
    if not predictor:
        return jsonify({"error": "Predictor not available"}), 500
    
    try:
        data = request.get_json()
        team1 = data.get('team1')
        team2 = data.get('team2')
        venue = data.get('venue')
        toss_winner = data.get('tossWinner')
        toss_decision = data.get('tossDecision')
        
        # Validate inputs
        if not all([team1, team2, venue, toss_winner, toss_decision]):
            return jsonify({"error": "Missing required parameters"}), 400
        
        if team1 == team2:
            return jsonify({"error": "Team 1 and Team 2 cannot be the same"}), 400
        
        result = predictor.predict_match(team1, team2, venue, toss_winner, toss_decision)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route('/api/team-stats/<team>')
def get_team_stats_api(team):
    """API endpoint to get team statistics."""
    if not data_processor:
        return jsonify({"error": "Data processor not available"}), 500
    
    try:
        team_stats = data_processor.get_team_stats(team)
        return jsonify(team_stats)
    except Exception as e:
        logger.error(f"Team stats error: {e}")
        return jsonify({"error": f"Failed to get team stats: {str(e)}"}), 500

@app.route('/api/venue-stats/<venue>')
def get_venue_stats_api(venue):
    """API endpoint to get venue statistics."""
    if not data_processor:
        return jsonify({"error": "Data processor not available"}), 500
    
    try:
        venue_stats = data_processor.get_venue_stats(venue)
        return jsonify(venue_stats)
    except Exception as e:
        logger.error(f"Venue stats error: {e}")
        return jsonify({"error": f"Failed to get venue stats: {str(e)}"}), 500

@app.route('/api/head-to-head/<team1>/<team2>')
def get_head_to_head_api(team1, team2):
    """API endpoint to get head-to-head statistics between two teams."""
    if not data_processor:
        return jsonify({"error": "Data processor not available"}), 500
    
    try:
        h2h_stats = data_processor.get_head_to_head_specific(team1, team2)
        return jsonify(h2h_stats)
    except Exception as e:
        logger.error(f"Head-to-head stats error: {e}")
        return jsonify({"error": f"Failed to get head-to-head stats: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
