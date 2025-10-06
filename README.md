# Ghost Personality Test 👻

A modern, interactive Flask web application that predicts user personality based on yes/no questions with a stunning ghost-themed UI.

## Features

✨ **Machine Learning Prediction**: Uses scikit-learn to predict personality types based on user responses
🎨 **Beautiful Ghost-Themed UI**: Modern, animated interface with floating ghosts and smooth transitions
📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
🌟 **Dynamic Interactions**: Smooth animations and ghost-themed visual effects
📊 **Detailed Results**: Shows personality type with trait scores and key characteristics

## Personality Types

- 🌟 **The Adventurer** - Spontaneous, outgoing, and optimistic
- 🧠 **The Analyst** - Logical, organized, and analytical
- 💝 **The Diplomat** - Empathetic, social, and caring
- 🛡️ **The Sentinel** - Reliable, organized, and practical
- 🔍 **The Explorer** - Curious, flexible, and adventurous

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
d:\random\
├── app.py                 # Main Flask application
├── ml_model.py           # Machine learning model for personality prediction
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Main HTML template
└── static/
    └── css/
        └── style.css    # Styling and animations
```

## How It Works

1. **User answers 10 yes/no questions** with an interactive ghost-themed interface
2. **Machine learning model analyzes responses** using a Decision Tree Classifier
3. **Personality prediction is generated** with detailed trait scores
4. **Results are displayed** with beautiful animations and visual feedback

## Technologies Used

- **Backend**: Flask (Python web framework)
- **ML Model**: scikit-learn (Decision Tree Classifier)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradients, animations, and glassmorphism effects
- **Fonts**: Google Fonts (Poppins)

## Customization

You can customize:
- Questions in `app.py` (QUESTIONS list)
- Personality types and descriptions in `ml_model.py`
- Colors and animations in `static/css/style.css`
- Training data for the ML model in `ml_model.py`

Enjoy discovering your personality! 👻✨
