import numpy as np

def estimate_confidence(answer: str):
    length = len(answer.split())
    confidence = max(0.4, min(0.95, 1 - (1 / (length + 1))))
    return round(confidence * 100, 2)
