#!/usr/bin/env python3
"""
Simple test script to verify the API endpoints work correctly
"""

import requests
import json

API_BASE = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get(f"{API_BASE}/health")
        print(f"Health check: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_mbti_questions():
    """Test MBTI questions endpoint"""
    try:
        response = requests.get(f"{API_BASE}/questions/mbti?num_questions=5")
        print(f"MBTI Questions: {response.status_code}")
        data = response.json()
        print(f"Got {len(data)} questions")
        return response.status_code == 200
    except Exception as e:
        print(f"MBTI questions test failed: {e}")
        return False

def test_ocean_questions():
    """Test OCEAN questions endpoint"""
    try:
        response = requests.get(f"{API_BASE}/questions/ocean?num_questions=10")
        print(f"OCEAN Questions: {response.status_code}")
        data = response.json()
        print(f"Got {len(data)} questions")
        return response.status_code == 200
    except Exception as e:
        print(f"OCEAN questions test failed: {e}")
        return False

def test_mbti_prediction():
    """Test MBTI prediction endpoint"""
    try:
        answers = [
            {"question_id": 1, "answer": "Meet new people and engage in conversations"},
            {"question_id": 2, "answer": "Logical analysis and objective facts"},
            {"question_id": 3, "answer": "Structured with clear deadlines and procedures"},
            {"question_id": 4, "answer": "Start with the big picture and work down to details"},
            {"question_id": 5, "answer": "Focus on finding the most logical solution"}
        ]
        
        response = requests.post(
            f"{API_BASE}/predict/mbti",
            headers={"Content-Type": "application/json"},
            data=json.dumps(answers)
        )
        print(f"MBTI Prediction: {response.status_code}")
        data = response.json()
        print(f"Predicted type: {data.get('mbti_type')}")
        print(f"Confidence: {data.get('confidence')}")
        return response.status_code == 200
    except Exception as e:
        print(f"MBTI prediction test failed: {e}")
        return False

def test_ocean_prediction():
    """Test OCEAN prediction endpoint"""
    try:
        answers = [
            {"question_id": 1, "answer": 4},
            {"question_id": 2, "answer": 3},
            {"question_id": 3, "answer": 5},
            {"question_id": 4, "answer": 2},
            {"question_id": 5, "answer": 4}
        ]
        
        response = requests.post(
            f"{API_BASE}/predict/ocean",
            headers={"Content-Type": "application/json"},
            data=json.dumps(answers)
        )
        print(f"OCEAN Prediction: {response.status_code}")
        data = response.json()
        print(f"Scores: {data.get('scores')}")
        return response.status_code == 200
    except Exception as e:
        print(f"OCEAN prediction test failed: {e}")
        return False

def main():
    print("=== API Testing ===")
    
    tests = [
        ("Health Check", test_health),
        ("MBTI Questions", test_mbti_questions),
        ("OCEAN Questions", test_ocean_questions),
        ("MBTI Prediction", test_mbti_prediction),
        ("OCEAN Prediction", test_ocean_prediction)
    ]
    
    passed = 0
    for name, test_func in tests:
        print(f"\n--- {name} ---")
        if test_func():
            passed += 1
            print("✓ PASSED")
        else:
            print("✗ FAILED")
    
    print(f"\n=== Results: {passed}/{len(tests)} tests passed ===")

if __name__ == "__main__":
    main()
