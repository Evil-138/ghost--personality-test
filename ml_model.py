import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

class PersonalityPredictor:
    def __init__(self):
        """Initialize the personality prediction model"""
        self.model = DecisionTreeClassifier(random_state=42, max_depth=5)
        self.scaler = StandardScaler()
        self.personality_types = {
            0: "The Adventurer",
            1: "The Analyst",
            2: "The Diplomat",
            3: "The Sentinel",
            4: "The Explorer"
        }
        self._train_model()
    
    def _train_model(self):
        """Train the model with sample data"""
        # Generate synthetic training data (10 questions, yes=1, no=0)
        # Each row represents a personality pattern
        X_train = np.array([
            # The Adventurer - outgoing, spontaneous, optimistic
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            
            # The Analyst - logical, organized, introverted
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            
            # The Diplomat - empathetic, social, feeling-based
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
            
            # The Sentinel - organized, routine-loving, cautious
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            
            # The Explorer - curious, flexible, adventurous
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        ])
        
        y_train = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
        
        # Train the model
        self.model.fit(X_train, y_train)
    
    def predict(self, answers):
        """
        Predict personality type based on yes/no answers
        
        Args:
            answers: List of 10 binary values (1 for yes, 0 for no)
        
        Returns:
            Dictionary with personality type and description
        """
        answers_array = np.array(answers).reshape(1, -1)
        prediction = self.model.predict(answers_array)[0]
        
        personality_descriptions = {
            0: {
                "type": "The Adventurer",
                "description": "You're spontaneous, outgoing, and love new experiences! You bring energy and excitement wherever you go.",
                "traits": ["Spontaneous", "Optimistic", "Social", "Energetic"],
                "emoji": "🌟"
            },
            1: {
                "type": "The Analyst",
                "description": "You're logical, organized, and thoughtful. You excel at problem-solving and strategic thinking.",
                "traits": ["Logical", "Organized", "Analytical", "Strategic"],
                "emoji": "🧠"
            },
            2: {
                "type": "The Diplomat",
                "description": "You're empathetic, social, and caring. You excel at understanding others and building connections.",
                "traits": ["Empathetic", "Social", "Caring", "Intuitive"],
                "emoji": "💝"
            },
            3: {
                "type": "The Sentinel",
                "description": "You're reliable, organized, and practical. You value stability and take your responsibilities seriously.",
                "traits": ["Reliable", "Organized", "Practical", "Responsible"],
                "emoji": "🛡️"
            },
            4: {
                "type": "The Explorer",
                "description": "You're curious, flexible, and love adventure. You're always seeking new knowledge and experiences.",
                "traits": ["Curious", "Flexible", "Adventurous", "Creative"],
                "emoji": "🔍"
            }
        }
        
        return personality_descriptions.get(prediction, personality_descriptions[0])
    
    def get_personality_traits(self, answers):
        """
        Analyze individual traits from answers
        
        Returns:
            Dictionary with trait scores
        """
        traits = {
            "extroversion": (answers[0] + answers[6] + (1 - answers[1])) / 3 * 100,
            "organization": (answers[2] + answers[7]) / 2 * 100,
            "openness": (answers[4] + (1 - answers[7])) / 2 * 100,
            "emotional_stability": (1 - answers[3] + answers[5]) / 2 * 100,
            "empathy": (answers[8] + (1 - answers[9])) / 2 * 100
        }
        
        return {k: round(v, 1) for k, v in traits.items()}
