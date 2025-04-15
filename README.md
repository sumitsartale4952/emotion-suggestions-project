# Emotion Suggestions Project

This project uses speech emotion recognition (SER) to detect a user's emotional state from their speech and then provides personalized suggestions (like listening to music or playing games) to improve their mood.

## Overview
- **SER Module:** Processes audio input and classifies emotions (happy, sad, angry).
- **Suggestions Module:** Maps the detected emotion to a list of recommended activities.
- **Deployment:** Dockerized and ready for integration.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app/main.py`
3. Access the web interface at `http://localhost:5000`

## Project Structure
```
emotion-suggestions-project/
├── app/
│   ├── ser/
│   │   ├── emotion_classifier.py  # Speech emotion recognition model
│   │   ├── models/               # Trained model files
│   │   │   ├── model.h5
│   │   │   └── model_metadata.json
│   ├── suggestions/
│   │   ├── recommendation_engine.py  # Suggestion generation logic
│   │   └── data/
│   │       └── games_data.csv    # Game suggestions database
│   ├── ui/
│   │   ├── index.html           # Web interface
│   │   ├── styles.css
│   │   └── script.js
│   └── main.py                  # Flask application entry point
├── data/
│   └── Audio_data/              # Directory for audio processing
├── tests/                       # Unit tests
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
└── README.md
```

## Features
- Real-time speech emotion recognition
- Personalized activity suggestions based on emotional state
- Web-based user interface
- RESTful API endpoints for integration
- Docker support for easy deployment

## API Endpoints
- `GET /` - Serves the web interface
- `POST /predict` - Accepts audio file, returns emotion and suggestions
  ```json
  {
    "emotion": "happy",
    "suggestions": ["Play action games", "Listen to upbeat music"]
  }
  ```

## Dependencies
- Python 3.8+
- TensorFlow 2.x
- Flask
- librosa
- numpy
- pandas

## Development
1. Clone the repository:
```bash
git clone https://github.com/yourusername/emotion-suggestions-project.git
cd emotion-suggestions-project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
python -m pytest tests/
```

## Docker Deployment
1. Build the container:
```bash
docker build -t emotion-suggestions .
```

2. Run the container:
```bash
docker run -p 5000:5000 emotion-suggestions
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Authors
- Your Name
- Contributors

## Acknowledgments
- Speech emotion recognition model based on the RAVDESS dataset
- Flask web framework
- TensorFlow and Keras teams
