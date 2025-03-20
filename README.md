# IPL Analyzer

A Flask-based web application for analyzing Indian Premier League (IPL) cricket matches, providing team statistics, venue analysis, and match outcome predictions using machine learning.

## Features

- **Match Prediction**: Predict match outcomes based on historical data, team performance, and venue statistics
- **Team Analysis**: Detailed statistics and performance metrics for all IPL teams
- **Venue Statistics**: Comprehensive analysis of match outcomes at different venues
- **Head-to-Head Comparisons**: Compare performance statistics between any two teams
- **Interactive UI**: Modern, responsive interface with dynamic data visualization

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Pandas, Scikit-learn
- **Visualization**: Chart.js

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IPLAnalyzer.git
   cd IPLAnalyzer
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
├── app.py                 # Main Flask application
├── utils/
│   ├── data_processor.py  # Data processing utilities
│   └── predictor.py       # Match prediction model
├── templates/             # HTML templates
├── static/               # Static assets (CSS, JS)
└── attached_assets/      # Data files
```

## Features in Detail

### Match Prediction
- Input match parameters including teams, venue, and toss details
- Get win probability predictions based on historical data
- View detailed reasoning behind predictions

### Team Analysis
- Overall team performance metrics
- Win/loss ratios
- Performance trends over seasons
- Head-to-head statistics

### Venue Statistics
- Match outcomes by venue
- Team performance at specific venues
- Toss decision impact analysis

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- IPL match data sourced from reliable cricket statistics databases
- Built with inspiration from cricket analytics platforms
- Special thanks to the open-source community for various tools and libraries used in this project