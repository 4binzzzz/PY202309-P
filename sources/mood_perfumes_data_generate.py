import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer


file_path = 'data/perfume_data_new.csv'  
perfume_data = pd.read_csv(file_path)

#텍스트 전처리
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

#Description 전처리
perfume_data['Processed_Description'] = perfume_data['Description'].apply(preprocess_text)

# TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(perfume_data['Processed_Description'])

#감정-키워드 매핑
emotion_keywords = {
    'happiness': ['happy', 'joy', 'bright', 'light', 'fresh'],
    'sadness': ['sad', 'melancholic', 'deep', 'dark', 'heavy'],
    'anger': ['intense', 'strong', 'spicy', 'bold', 'sharp'],
    'calmness': ['calm', 'soft', 'soothing', 'gentle', 'smooth'],
    'love': ['passionate', 'romantic', 'sweet', 'warm', 'sensual']
}

#감정에 따라 분류
perfume_data['Emotion'] = 'other'
for emotion, keywords in emotion_keywords.items():
    for index, row in perfume_data.iterrows():
        if any(keyword in row['Processed_Description'] for keyword in keywords):
            perfume_data.at[index, 'Emotion'] = emotion


perfume_data.to_csv('data/mood_perfumes_data.csv', index=False)
