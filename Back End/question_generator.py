import random
from typing import List, Dict, Any

class QuestionGenerator:
    def __init__(self):
        self.mbti_questions = self._load_mbti_questions()
        self.ocean_questions = self._load_ocean_questions()
    
    def _load_mbti_questions(self) -> List[Dict[str, Any]]:
        """Load MBTI-specific questions"""
        return [
            {
                "id": 1,
                "text": "At a party, you would most likely:",
                "options": [
                    "Meet new people and engage in conversations",
                    "Have deep conversations with a few close friends",
                    "Observe the crowd and analyze social dynamics",
                    "Take charge and organize activities"
                ],
                "dimensions": ["E", "I", "N", "S"]
            },
            {
                "id": 2,
                "text": "When making important decisions, you primarily rely on:",
                "options": [
                    "Logical analysis and objective facts",
                    "Personal values and how it affects others",
                    "Past experiences and proven methods",
                    "Future possibilities and innovative approaches"
                ],
                "dimensions": ["T", "F", "S", "N"]
            },
            {
                "id": 3,
                "text": "Your ideal work environment would be:",
                "options": [
                    "Structured with clear deadlines and procedures",
                    "Flexible with room for creativity and spontaneity",
                    "Collaborative with lots of team interaction",
                    "Quiet and focused with minimal interruptions"
                ],
                "dimensions": ["J", "P", "E", "I"]
            },
            {
                "id": 4,
                "text": "When learning something new, you prefer to:",
                "options": [
                    "Start with the big picture and work down to details",
                    "Start with specific details and build up to the big picture",
                    "Learn through hands-on practice and experimentation",
                    "Learn through reading and theoretical study"
                ],
                "dimensions": ["N", "S", "S", "N"]
            },
            {
                "id": 5,
                "text": "In a conflict, you tend to:",
                "options": [
                    "Focus on finding the most logical solution",
                    "Focus on how everyone feels and finding harmony",
                    "Address the issue directly and quickly",
                    "Take time to understand all perspectives first"
                ],
                "dimensions": ["T", "F", "E", "I"]
            },
            {
                "id": 6,
                "text": "You feel most energized when:",
                "options": [
                    "Working on multiple projects simultaneously",
                    "Focusing deeply on one complex problem",
                    "Collaborating with others on shared goals",
                    "Working independently on your own ideas"
                ],
                "dimensions": ["P", "J", "E", "I"]
            },
            {
                "id": 7,
                "text": "When planning a vacation, you would:",
                "options": [
                    "Create a detailed itinerary with reservations",
                    "Keep it flexible and see what happens",
                    "Research extensively and plan every detail",
                    "Go with the flow and be spontaneous"
                ],
                "dimensions": ["J", "P", "J", "P"]
            },
            {
                "id": 8,
                "text": "You prefer to receive feedback that is:",
                "options": [
                    "Direct and honest, even if it's harsh",
                    "Gentle and considerate of your feelings",
                    "Specific and detailed with examples",
                    "General and focused on potential"
                ],
                "dimensions": ["T", "F", "S", "N"]
            },
            {
                "id": 9,
                "text": "In a group project, you naturally:",
                "options": [
                    "Take on a leadership role and delegate tasks",
                    "Support others and help them succeed",
                    "Focus on the technical details and quality",
                    "Generate creative ideas and solutions"
                ],
                "dimensions": ["E", "F", "S", "N"]
            },
            {
                "id": 10,
                "text": "You feel most comfortable when:",
                "options": [
                    "You have a clear plan and know what's coming",
                    "You have flexibility and can adapt as needed",
                    "You're surrounded by people who understand you",
                    "You have time alone to process your thoughts"
                ],
                "dimensions": ["J", "P", "E", "I"]
            },
            {
                "id": 11,
                "text": "When working on a project, you prefer to:",
                "options": [
                    "Start immediately and figure things out as you go",
                    "Plan everything thoroughly before starting",
                    "Collaborate with others throughout the process",
                    "Work alone and present the final result"
                ],
                "dimensions": ["P", "J", "E", "I"]
            },
            {
                "id": 12,
                "text": "Your ideal learning environment is:",
                "options": [
                    "A quiet library with minimal distractions",
                    "A bustling coffee shop with background noise",
                    "A structured classroom with clear instructions",
                    "An open space where you can move around"
                ],
                "dimensions": ["I", "E", "S", "N"]
            },
            {
                "id": 13,
                "text": "When someone asks for your opinion, you:",
                "options": [
                    "Give a direct, honest answer immediately",
                    "Consider their feelings before responding",
                    "Ask clarifying questions to understand the context",
                    "Take time to think through all possibilities"
                ],
                "dimensions": ["T", "F", "S", "N"]
            },
            {
                "id": 14,
                "text": "You're most productive when:",
                "options": [
                    "You have a strict schedule to follow",
                    "You can work at your own pace",
                    "You're surrounded by motivated people",
                    "You have complete silence and solitude"
                ],
                "dimensions": ["J", "P", "E", "I"]
            },
            {
                "id": 15,
                "text": "When facing a complex problem, you:",
                "options": [
                    "Break it down into smaller, manageable parts",
                    "Look for patterns and connections",
                    "Ask others for their perspectives",
                    "Trust your intuition and go with your gut"
                ],
                "dimensions": ["S", "N", "E", "N"]
            },
            {
                "id": 16,
                "text": "Your ideal weekend would be:",
                "options": [
                    "A planned itinerary with activities and reservations",
                    "A spontaneous adventure with no set plans",
                    "Social gatherings with friends and family",
                    "Quiet time at home with books or hobbies"
                ],
                "dimensions": ["J", "P", "E", "I"]
            },
            {
                "id": 17,
                "text": "When making important life decisions, you:",
                "options": [
                    "Research extensively and weigh all options",
                    "Follow your heart and personal values",
                    "Seek advice from trusted friends and family",
                    "Trust your instincts and make quick decisions"
                ],
                "dimensions": ["S", "F", "E", "N"]
            },
            {
                "id": 18,
                "text": "You feel most energized after:",
                "options": [
                    "A day of socializing and meeting new people",
                    "A quiet day of reflection and introspection",
                    "Completing a challenging task successfully",
                    "Exploring new ideas and possibilities"
                ],
                "dimensions": ["E", "I", "S", "N"]
            },
            {
                "id": 19,
                "text": "When someone disagrees with you, you:",
                "options": [
                    "Present logical arguments to convince them",
                    "Try to understand their perspective first",
                    "Avoid conflict and change the subject",
                    "Engage in a lively debate to explore both sides"
                ],
                "dimensions": ["T", "F", "F", "T"]
            },
            {
                "id": 20,
                "text": "Your ideal work schedule would be:",
                "options": [
                    "Fixed hours with clear start and end times",
                    "Flexible hours based on your energy levels",
                    "Regular hours with frequent social interaction",
                    "Variable hours that allow for deep focus periods"
                ],
                "dimensions": ["J", "P", "E", "I"]
            }
        ]
    
    def _load_ocean_questions(self) -> List[Dict[str, Any]]:
        """Load OCEAN-specific questions"""
        return [
            {
                "id": 1,
                "text": "I am the life of the party",
                "options": [
                    "Strongly Disagree",
                    "Disagree", 
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": False
            },
            {
                "id": 2,
                "text": "I feel comfortable around people",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral", 
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": False
            },
            {
                "id": 3,
                "text": "I start conversations",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree", 
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": False
            },
            {
                "id": 4,
                "text": "I don't talk a lot",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": True
            },
            {
                "id": 5,
                "text": "I think a lot",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "O",
                "reverse": False
            },
            {
                "id": 6,
                "text": "I have difficulty understanding abstract ideas",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "O",
                "reverse": True
            },
            {
                "id": 7,
                "text": "I have a vivid imagination",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "O",
                "reverse": False
            },
            {
                "id": 8,
                "text": "I am not interested in abstract ideas",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "O",
                "reverse": True
            },
            {
                "id": 9,
                "text": "I have excellent ideas",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "O",
                "reverse": False
            },
            {
                "id": 10,
                "text": "I am always prepared",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 11,
                "text": "I pay attention to details",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 12,
                "text": "I get chores done right away",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 13,
                "text": "I like order",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 14,
                "text": "I follow a schedule",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 15,
                "text": "I am exacting in my work",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": False
            },
            {
                "id": 16,
                "text": "I leave my belongings around",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": True
            },
            {
                "id": 17,
                "text": "I make a mess of things",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": True
            },
            {
                "id": 18,
                "text": "I often forget to put things back in their proper place",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": True
            },
            {
                "id": 19,
                "text": "I shirk my duties",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "C",
                "reverse": True
            },
            {
                "id": 20,
                "text": "I am interested in people",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": False
            },
            {
                "id": 21,
                "text": "I feel others' emotions",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": False
            },
            {
                "id": 22,
                "text": "I have a soft heart",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": False
            },
            {
                "id": 23,
                "text": "I am not really interested in others",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": True
            },
            {
                "id": 24,
                "text": "I am not interested in other people's problems",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": True
            },
            {
                "id": 25,
                "text": "I feel little concern for others",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "A",
                "reverse": True
            },
            {
                "id": 26,
                "text": "I am hard to get to know",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": True
            },
            {
                "id": 27,
                "text": "I am quiet around strangers",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": True
            },
            {
                "id": 28,
                "text": "I don't like to draw attention to myself",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": True
            },
            {
                "id": 29,
                "text": "I don't mind being the center of attention",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "E",
                "reverse": False
            },
            {
                "id": 30,
                "text": "I get stressed out easily",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 31,
                "text": "I am relaxed most of the time",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": True
            },
            {
                "id": 32,
                "text": "I worry about things",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 33,
                "text": "I seldom feel blue",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": True
            },
            {
                "id": 34,
                "text": "I am easily disturbed",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 35,
                "text": "I get upset easily",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 36,
                "text": "I change my mood a lot",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 37,
                "text": "I have frequent mood swings",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 38,
                "text": "I get irritated easily",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            },
            {
                "id": 39,
                "text": "I often feel blue",
                "options": [
                    "Strongly Disagree",
                    "Disagree",
                    "Neutral",
                    "Agree",
                    "Strongly Agree"
                ],
                "dimension": "N",
                "reverse": False
            }
        ]
    
    def get_mbti_questions(self, num_questions: int = 20) -> List[Dict[str, Any]]:
        """Get a random sample of MBTI questions"""
        return random.sample(self.mbti_questions, min(num_questions, len(self.mbti_questions)))
    
    def get_ocean_questions(self, num_questions: int = 40) -> List[Dict[str, Any]]:
        """Get a random sample of OCEAN questions"""
        return random.sample(self.ocean_questions, min(num_questions, len(self.ocean_questions)))
    
    def calculate_mbti_score(self, answers: List[str]) -> tuple[str, dict]:
        """Calculate MBTI type from answers"""
        # Simple scoring system based on question dimensions
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
        for i, answer in enumerate(answers):
            if i < len(self.mbti_questions):
                question = self.mbti_questions[i]
                if "dimensions" in question:
                    # Map answer to dimension
                    option_index = question["options"].index(answer) if answer in question["options"] else 0
                    dimension = question["dimensions"][option_index]
                    scores[dimension] += 1
        
        # Calculate percentages for each dimension
        total_questions = len(answers)
        breakdown = {}
        for dimension in scores:
            breakdown[dimension] = scores[dimension] / total_questions if total_questions > 0 else 0.5
        
        # Determine MBTI type
        mbti = ""
        mbti += "E" if scores["E"] > scores["I"] else "I"
        mbti += "S" if scores["S"] > scores["N"] else "N"
        mbti += "T" if scores["T"] > scores["F"] else "F"
        mbti += "J" if scores["J"] > scores["P"] else "P"
        
        # Calculate confidence based on how clear the preferences are
        confidence = 0.5
        for pair in [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]:
            diff = abs(scores[pair[0]] - scores[pair[1]])
            confidence += diff / (total_questions * 2)  # Max 0.125 per pair
        
        return mbti, breakdown, min(confidence, 1.0)
    
    def calculate_ocean_scores(self, answers: List[int]) -> Dict[str, float]:
        """Calculate OCEAN scores from answers"""
        scores = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
        counts = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
        
        for i, answer in enumerate(answers):
            if i < len(self.ocean_questions):
                question = self.ocean_questions[i]
                dimension = question["dimension"]
                reverse = question["reverse"]
                
                # Adjust score based on reverse scoring
                score = answer if not reverse else (6 - answer)
                scores[dimension] += score
                counts[dimension] += 1
        
        # Calculate averages
        for dimension in scores:
            if counts[dimension] > 0:
                scores[dimension] = scores[dimension] / counts[dimension]
        
        return scores
