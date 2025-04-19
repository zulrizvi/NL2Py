import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
data = pd.read_csv("data/training_data.csv")

X = data["sentence"]
Y = data["intent"]

model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', LogisticRegression())
])


model.fit(X,Y)
joblib.dump(model, "model/intent_classifier.pkl")
print("✅ Model trained and saved!")