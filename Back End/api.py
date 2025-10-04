from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os
import numpy as np
from data_loader import DatasetLoader
from models import MBTIModel, OCEANModel
from question_generator import QuestionGenerator
from config import MODEL_SAVE_PATH

app = FastAPI(title="Personality Assessment API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models and data
mbti_model = None
ocean_model = None
question_generator = QuestionGenerator()
data_loader = DatasetLoader()

# Pydantic models for request/response
class QuestionResponse(BaseModel):
    id: int
    text: str
    options: List[str]
    multipleChoice: Optional[bool] = False

class MBTIAnswer(BaseModel):
    question_id: int
    answer: str

class OCEANAnswer(BaseModel):
    question_id: int
    answer: int  # 1-5 scale

class MBTIResult(BaseModel):
    mbti_type: str
    confidence: float
    breakdown: Dict[str, float]

class OCEANResult(BaseModel):
    scores: Dict[str, float]
    interpretation: Dict[str, str]

@app.on_event("startup")
async def startup_event():
    """Initialize models on startup"""
    global mbti_model, ocean_model
    
    # Create models directory
    os.makedirs(MODEL_SAVE_PATH, exist_ok=True)
    
    # Try to load existing models
    mbti_path = os.path.join(MODEL_SAVE_PATH, "mbti_model.pkl")
    ocean_path = os.path.join(MODEL_SAVE_PATH, "ocean_model.pkl")
    
    if os.path.exists(mbti_path):
        mbti_model = MBTIModel()
        mbti_model.load(mbti_path)
        print("Loaded existing MBTI model")
    else:
        print("No existing MBTI model found. Train models first.")
    
    if os.path.exists(ocean_path):
        ocean_model = OCEANModel()
        ocean_model.load(ocean_path)
        print("Loaded existing OCEAN model")
    else:
        print("No existing OCEAN model found. Train models first.")

@app.get("/")
async def root():
    return {"message": "Personality Assessment API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "mbti_model_loaded": mbti_model is not None, "ocean_model_loaded": ocean_model is not None}

@app.post("/train-models")
async def train_models():
    """Train both MBTI and OCEAN models"""
    try:
        # Download and preprocess data
        print("Downloading and preprocessing data...")
        mbti_X, mbti_y, mbti_features = data_loader.download_mbti_dataset()
        ocean_X, ocean_y, ocean_features, ocean_cols = data_loader.download_ocean_dataset()
        
        # Train MBTI model
        global mbti_model
        mbti_model = MBTIModel()
        mbti_accuracy = mbti_model.train(mbti_X, mbti_y)
        mbti_model.save(os.path.join(MODEL_SAVE_PATH, "mbti_model.pkl"))
        
        # Train OCEAN model
        global ocean_model
        ocean_model = OCEANModel()
        ocean_mse = ocean_model.train(ocean_X, ocean_y)
        ocean_model.save(os.path.join(MODEL_SAVE_PATH, "ocean_model.pkl"))
        
        return {
            "message": "Models trained successfully",
            "mbti_accuracy": mbti_accuracy,
            "ocean_mse": ocean_mse
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error training models: {str(e)}")

@app.get("/questions/mbti")
async def get_mbti_questions(num_questions: int = 20) -> List[QuestionResponse]:
    """Get MBTI questions"""
    questions = question_generator.get_mbti_questions(num_questions)
    return [QuestionResponse(**q) for q in questions]

@app.get("/questions/ocean")
async def get_ocean_questions(num_questions: int = 40) -> List[QuestionResponse]:
    """Get OCEAN questions"""
    questions = question_generator.get_ocean_questions(num_questions)
    return [QuestionResponse(**q) for q in questions]

@app.post("/predict/mbti")
async def predict_mbti(answers: List[MBTIAnswer]) -> MBTIResult:
    """Predict MBTI type from answers"""
    if mbti_model is None:
        raise HTTPException(status_code=400, detail="MBTI model not trained yet")
    
    try:
        # Convert answers to feature vector
        # This is a simplified version - in practice, you'd need to map answers to numerical values
        feature_vector = np.array([[1, 2, 3, 4, 5] * 10])  # Placeholder
        
        # Use question generator for simple scoring
        answer_texts = [a.answer for a in answers]
        mbti_type, breakdown, confidence = question_generator.calculate_mbti_score(answer_texts)
        
        return MBTIResult(
            mbti_type=mbti_type,
            confidence=confidence,
            breakdown=breakdown
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting MBTI: {str(e)}")

@app.post("/predict/ocean")
async def predict_ocean(answers: List[OCEANAnswer]) -> OCEANResult:
    """Predict OCEAN scores from answers"""
    if ocean_model is None:
        raise HTTPException(status_code=400, detail="OCEAN model not trained yet")
    
    try:
        # Convert answers to numerical scores
        answer_scores = [a.answer for a in answers]
        
        # Use question generator for simple scoring
        scores = question_generator.calculate_ocean_scores(answer_scores)
        
        # Generate interpretation
        interpretation = {}
        for trait, score in scores.items():
            if trait == "O":
                interpretation[trait] = "High Openness" if score > 3.5 else "Low Openness"
            elif trait == "C":
                interpretation[trait] = "High Conscientiousness" if score > 3.5 else "Low Conscientiousness"
            elif trait == "E":
                interpretation[trait] = "High Extraversion" if score > 3.5 else "Low Extraversion"
            elif trait == "A":
                interpretation[trait] = "High Agreeableness" if score > 3.5 else "Low Agreeableness"
            elif trait == "N":
                interpretation[trait] = "High Neuroticism" if score > 3.5 else "Low Neuroticism"
        
        return OCEANResult(
            scores=scores,
            interpretation=interpretation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting OCEAN: {str(e)}")

@app.get("/mbti-types")
async def get_mbti_types():
    """Get information about MBTI types"""
    return {
        "types": [
            {"code": "INTJ", "name": "The Architect", "description": "Imaginative and strategic thinkers"},
            {"code": "INTP", "name": "The Thinker", "description": "Innovative inventors with an unquenchable thirst for knowledge"},
            {"code": "ENTJ", "name": "The Commander", "description": "Bold, imaginative and strong-willed leaders"},
            {"code": "ENTP", "name": "The Debater", "description": "Smart and curious thinkers who cannot resist an intellectual challenge"},
            {"code": "INFJ", "name": "The Advocate", "description": "Creative and insightful, inspired by their own values"},
            {"code": "INFP", "name": "The Mediator", "description": "Poetic, kind and altruistic people"},
            {"code": "ENFJ", "name": "The Protagonist", "description": "Charismatic and inspiring leaders"},
            {"code": "ENFP", "name": "The Campaigner", "description": "Enthusiastic, creative and sociable free spirits"},
            {"code": "ISTJ", "name": "The Logistician", "description": "Practical and fact-minded, reliable"},
            {"code": "ISFJ", "name": "The Protector", "description": "Very dedicated and warm protectors"},
            {"code": "ESTJ", "name": "The Executive", "description": "Excellent administrators, unsurpassed at managing things"},
            {"code": "ESFJ", "name": "The Consul", "description": "Extraordinarily caring, social and popular"},
            {"code": "ISTP", "name": "The Virtuoso", "description": "Bold and practical experimenters"},
            {"code": "ISFP", "name": "The Adventurer", "description": "Flexible and charming artists"},
            {"code": "ESTP", "name": "The Entrepreneur", "description": "Smart, energetic and very perceptive people"},
            {"code": "ESFP", "name": "The Entertainer", "description": "Spontaneous, energetic and enthusiastic people"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
