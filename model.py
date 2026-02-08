import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_model():
    # 1. Ambil data laporan rakyat
    df = pd.read_csv('database.csv')
    
    # 2. Proses teks
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    
    # 3. Latih AI
    model = MultinomialNB()
    model.fit(X, df['label'])
    
    # 4. Simpan 'otak' AI yang dah pandai
    with open('ai_brain.pkl', 'wb') as f:
        pickle.dump((vectorizer, model), f)