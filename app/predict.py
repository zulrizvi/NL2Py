import joblib
model = joblib.load("model/intent_classifier.pkl")

def detect_intent_nltk(text):
    return model.predict([text])[0]