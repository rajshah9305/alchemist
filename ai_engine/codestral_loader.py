# ai_engine/codestral_loader.py
import os

def load_codestral_model():
    model_path = os.path.join(os.path.dirname(__file__), 'codestral_25.01.model')
    if not os.path.exists(model_path):
        raise FileNotFoundError("Codestral model not found. Please ensure the model file is in the ai_engine directory.")
    # Load the model (pseudo-code, replace with actual model loading)
    model = load_model_from_path(model_path)
    return model