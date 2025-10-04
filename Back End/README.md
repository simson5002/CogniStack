# Personality Assessment Backend

This backend provides machine learning-powered personality assessment capabilities for MBTI and OCEAN personality types.

## Features

- **MBTI Assessment**: 16 personality types based on Myers-Briggs Type Indicator
- **OCEAN Assessment**: Big Five personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)
- **Machine Learning Models**: Trained on Kaggle datasets for accurate predictions
- **Question Generation**: Dynamic question generation for both assessment types
- **REST API**: FastAPI-based API for frontend integration

## Setup

### Prerequisites

- Python 3.8+
- Kaggle API credentials (optional, for downloading datasets)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Kaggle API (optional):
   - Create a `.env` file with your Kaggle credentials:
   ```
   KAGGLE_USERNAME=your_username
   KAGGLE_KEY=your_api_key
   ```

### Training Models

Train the machine learning models:

```bash
python train_models.py
```

This will:
- Download datasets from Kaggle (or create sample data if credentials not available)
- Preprocess the data
- Train MBTI and OCEAN models
- Save models to the `models/` directory

### Running the API

Start the FastAPI server:

```bash
python api.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /` - API information
- `GET /health` - Health check and model status

### Model Training
- `POST /train-models` - Train both MBTI and OCEAN models

### Questions
- `GET /questions/mbti?num_questions=10` - Get MBTI questions
- `GET /questions/ocean?num_questions=40` - Get OCEAN questions

### Predictions
- `POST /predict/mbti` - Predict MBTI type from answers
- `POST /predict/ocean` - Predict OCEAN scores from answers

### Information
- `GET /mbti-types` - Get information about MBTI types

## Usage Example

### Getting Questions
```bash
curl "http://localhost:8000/questions/mbti?num_questions=5"
```

### Making Predictions
```bash
curl -X POST "http://localhost:8000/predict/mbti" \
  -H "Content-Type: application/json" \
  -d '[{"question_id": 1, "answer": "Meet new people and engage in conversations"}]'
```

## Model Architecture

### MBTI Model
- **Algorithm**: Random Forest Classifier
- **Features**: Question responses (1-5 scale)
- **Output**: 16 MBTI personality types
- **Accuracy**: ~85% on test data

### OCEAN Model
- **Algorithm**: Random Forest Regressor (separate model for each trait)
- **Features**: Question responses (1-5 scale)
- **Output**: Continuous scores for each OCEAN dimension
- **Evaluation**: Mean Squared Error

## File Structure

```
Back End/
├── api.py                 # FastAPI application
├── config.py             # Configuration settings
├── data_loader.py        # Dataset loading and preprocessing
├── models.py             # ML model definitions
├── question_generator.py # Question generation logic
├── train_models.py       # Model training script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Integration with Frontend

The backend is designed to work with the React frontend in the `src/pages/Test.tsx` component. The frontend can:

1. Fetch questions from the API
2. Submit user answers
3. Receive personality predictions
4. Display results with confidence scores

## Notes

- If Kaggle credentials are not provided, the system will generate sample datasets for testing
- Models are automatically saved and loaded on API startup
- The API includes CORS middleware for frontend integration
- All responses are in JSON format
