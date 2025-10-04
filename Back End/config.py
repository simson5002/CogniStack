import os
from dotenv import load_dotenv

load_dotenv()

# Kaggle API credentials
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME", "")
KAGGLE_KEY = os.getenv("KAGGLE_KEY", "")

# Dataset configurations
MBTI_DATASET = "danofer/compass"
OCEAN_DATASET = "tunguz/big-five-personality-test"

# Model configurations
MODEL_SAVE_PATH = "models"
DATA_PATH = "data"
