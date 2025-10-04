import os
import pandas as pd
import numpy as np
from kaggle.api.kaggle_api_extended import KaggleApi
from config import KAGGLE_USERNAME, KAGGLE_KEY, MBTI_DATASET, OCEAN_DATASET, DATA_PATH

class DatasetLoader:
    def __init__(self):
        self.api = KaggleApi()
        self.setup_kaggle()
        
    def setup_kaggle(self):
        """Setup Kaggle API credentials"""
        if KAGGLE_USERNAME and KAGGLE_KEY:
            os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)
            with open(os.path.expanduser("~/.kaggle/kaggle.json"), "w") as f:
                f.write(f'{{"username":"{KAGGLE_USERNAME}","key":"{KAGGLE_KEY}"}}')
            os.chmod(os.path.expanduser("~/.kaggle/kaggle.json"), 0o600)
        
        self.api.authenticate()
    
    def download_mbti_dataset(self):
        """Download and preprocess MBTI dataset"""
        print("Downloading MBTI dataset...")
        self.api.dataset_download_files(MBTI_DATASET, path=DATA_PATH, unzip=True)
        
        # Load the dataset
        mbti_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.csv')]
        mbti_df = None
        
        for file in mbti_files:
            if 'mbti' in file.lower() or 'personality' in file.lower():
                mbti_df = pd.read_csv(os.path.join(DATA_PATH, file))
                break
        
        if mbti_df is None:
            # Create a sample MBTI dataset if download fails
            print("Creating sample MBTI dataset...")
            mbti_df = self.create_sample_mbti_dataset()
        
        return self.preprocess_mbti_data(mbti_df)
    
    def download_ocean_dataset(self):
        """Download and preprocess OCEAN dataset"""
        print("Downloading OCEAN dataset...")
        self.api.dataset_download_files(OCEAN_DATASET, path=DATA_PATH, unzip=True)
        
        # Load the dataset
        ocean_files = [f for f in os.listdir(DATA_PATH) if f.endswith('.csv')]
        ocean_df = None
        
        for file in ocean_files:
            if 'big5' in file.lower() or 'ocean' in file.lower():
                ocean_df = pd.read_csv(os.path.join(DATA_PATH, file))
                break
        
        if ocean_df is None:
            # Create a sample OCEAN dataset if download fails
            print("Creating sample OCEAN dataset...")
            ocean_df = self.create_sample_ocean_dataset()
        
        return self.preprocess_ocean_data(ocean_df)
    
    def create_sample_mbti_dataset(self):
        """Create a sample MBTI dataset for testing"""
        np.random.seed(42)
        n_samples = 1000
        
        # Sample questions and responses
        questions = [
            "I prefer working in groups rather than alone",
            "I enjoy meeting new people at parties",
            "I like to plan things in advance",
            "I prefer facts over theories",
            "I make decisions based on logic",
            "I enjoy helping others with their problems",
            "I like to keep my options open",
            "I prefer structured environments",
            "I enjoy abstract thinking",
            "I like to be the center of attention",
            "I prefer routine over spontaneity",
            "I trust my instincts when making decisions",
            "I enjoy analyzing complex problems",
            "I like to work with my hands",
            "I prefer quiet environments",
            "I enjoy philosophical discussions"
        ]
        
        data = []
        for i in range(n_samples):
            # Generate random responses (1-5 scale)
            responses = np.random.randint(1, 6, len(questions))
            
            # Calculate MBTI type based on responses
            mbti_type = self.calculate_mbti_type(responses)
            
            row = {'type': mbti_type}
            for j, q in enumerate(questions):
                row[f'q{j+1}'] = responses[j]
            data.append(row)
        
        return pd.DataFrame(data)
    
    def create_sample_ocean_dataset(self):
        """Create a sample OCEAN dataset for testing"""
        np.random.seed(42)
        n_samples = 1000
        
        # OCEAN questions
        questions = [
            "I am the life of the party",
            "I feel comfortable around people",
            "I start conversations",
            "I talk to a lot of different people at parties",
            "I don't talk a lot",
            "I think a lot",
            "I have difficulty understanding abstract ideas",
            "I have a vivid imagination",
            "I am not interested in abstract ideas",
            "I have excellent ideas",
            "I am always prepared",
            "I pay attention to details",
            "I get chores done right away",
            "I like order",
            "I follow a schedule",
            "I am exacting in my work",
            "I leave my belongings around",
            "I make a mess of things",
            "I often forget to put things back in their proper place",
            "I shirk my duties",
            "I am interested in people",
            "I feel others' emotions",
            "I have a soft heart",
            "I am not really interested in others",
            "I am not interested in other people's problems",
            "I feel little concern for others",
            "I am hard to get to know",
            "I am quiet around strangers",
            "I don't like to draw attention to myself",
            "I don't mind being the center of attention"
        ]
        
        data = []
        for i in range(n_samples):
            # Generate random responses (1-5 scale)
            responses = np.random.randint(1, 6, len(questions))
            
            # Calculate OCEAN scores
            ocean_scores = self.calculate_ocean_scores(responses)
            
            row = {
                'O': ocean_scores[0],
                'C': ocean_scores[1], 
                'E': ocean_scores[2],
                'A': ocean_scores[3],
                'N': ocean_scores[4]
            }
            for j, q in enumerate(questions):
                row[f'q{j+1}'] = responses[j]
            data.append(row)
        
        return pd.DataFrame(data)
    
    def calculate_mbti_type(self, responses):
        """Calculate MBTI type from responses"""
        # Simple scoring system
        e_score = responses[0] + responses[1] + responses[9]  # Extraversion
        i_score = 15 - e_score  # Introversion
        
        s_score = responses[2] + responses[7] + responses[13]  # Sensing
        n_score = 15 - s_score  # Intuition
        
        t_score = responses[4] + responses[12] + responses[11]  # Thinking
        f_score = 15 - t_score  # Feeling
        
        j_score = responses[2] + responses[7] + responses[14]  # Judging
        p_score = 15 - j_score  # Perceiving
        
        mbti = ""
        mbti += "E" if e_score > i_score else "I"
        mbti += "S" if s_score > n_score else "N"
        mbti += "T" if t_score > f_score else "F"
        mbti += "J" if j_score > p_score else "P"
        
        return mbti
    
    def calculate_ocean_scores(self, responses):
        """Calculate OCEAN scores from responses"""
        # Openness (questions 6, 7, 8, 9, 10)
        openness = (responses[5] + (6-responses[6]) + responses[7] + (6-responses[8]) + responses[9]) / 5
        
        # Conscientiousness (questions 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        conscientiousness = (responses[10] + responses[11] + responses[12] + responses[13] + 
                           responses[14] + responses[15] + (6-responses[16]) + (6-responses[17]) + 
                           (6-responses[18]) + (6-responses[19])) / 10
        
        # Extraversion (questions 1, 2, 3, 4, 5)
        extraversion = (responses[0] + responses[1] + responses[2] + responses[3] + 
                       (6-responses[4])) / 5
        
        # Agreeableness (questions 21, 22, 23, 24, 25, 26)
        agreeableness = (responses[20] + responses[21] + responses[22] + (6-responses[23]) + 
                        (6-responses[24]) + (6-responses[25])) / 6
        
        # Neuroticism (questions 27, 28, 29, 30)
        neuroticism = (responses[26] + responses[27] + responses[28] + (6-responses[29])) / 4
        
        return [openness, conscientiousness, extraversion, agreeableness, neuroticism]
    
    def preprocess_mbti_data(self, df):
        """Preprocess MBTI dataset"""
        # Extract features (question responses)
        feature_cols = [col for col in df.columns if col.startswith('q')]
        X = df[feature_cols].values
        y = df['type'].values
        
        return X, y, feature_cols
    
    def preprocess_ocean_data(self, df):
        """Preprocess OCEAN dataset"""
        # Extract features (question responses)
        feature_cols = [col for col in df.columns if col.startswith('q')]
        X = df[feature_cols].values
        
        # Extract OCEAN scores as targets
        ocean_cols = ['O', 'C', 'E', 'A', 'N']
        y = df[ocean_cols].values
        
        return X, y, feature_cols, ocean_cols
