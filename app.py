from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from ml_model import PersonalityPredictor

app = Flask(__name__)

# Initialize the ML model
predictor = PersonalityPredictor()

# Personality questions
QUESTIONS = [
    "Do you enjoy being the center of attention?",
    "Do you prefer spending time alone rather than with others?",
    "Are you usually organized and plan ahead?",
    "Do you often feel anxious or worried?",
    "Do you enjoy trying new experiences?",
    "Are you generally optimistic about the future?",
    "Do you find it easy to start conversations with strangers?",
    "Do you prefer routine over spontaneity?",
    "Are you sensitive to others' emotions?",
    "Do you make decisions based on logic rather than feelings?"
]

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    answers = data.get('answers', [])
    
    if len(answers) != len(QUESTIONS):
        return jsonify({'error': 'Invalid number of answers'}), 400
    
    # Convert yes/no to 1/0
    binary_answers = [1 if ans.lower() == 'yes' else 0 for ans in answers]
    
    # Get prediction
    personality = predictor.predict(binary_answers)
    traits = predictor.get_personality_traits(binary_answers)
    
    return jsonify({
        'personality': personality,
        'traits': traits
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
