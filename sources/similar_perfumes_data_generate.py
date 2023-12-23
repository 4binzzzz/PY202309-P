## Keras_text to word sequence ##

import pandas as pd
from keras.preprocessing.text import text_to_word_sequence

#데이터 불러오기
file_path = 'data/perfume_data_new.csv'
perfume_data = pd.read_csv(file_path)

#결측치 있는 행을 제거 (Notes 열에 대해 80개의 결측치 존재)
perfume_data = perfume_data.dropna(subset=['Notes'])

#Notes를 단어 리스트로 변환
perfume_data['WordSequence'] = perfume_data['Notes'].apply(lambda x: text_to_word_sequence(x))

#단어 중복 유사도를 계산하는 함수
def word_overlap_similarity(word_seq1, word_seq2):
    set1 = set(word_seq1)
    set2 = set(word_seq2)
    return len(set1.intersection(set2))

#가장 유사한 향수 찾는 함수
def get_most_similar_perfume(name, df):
    #대상 향수의 단어 시퀀스를 가져오기
    target_word_seq = df[df['Name'] == name]['WordSequence'].iloc[0]

    #다른 향수들과의 유사도 계산
    similarities = []
    for _, row in df.iterrows():
        sim = word_overlap_similarity(target_word_seq, row['WordSequence'])
        similarities.append((row['Name'], sim))

    #유사도 점수를 기준으로 향수 정렬
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

    #자신을 제외하고 상위 5개 가져오기
    top_similar = [perfume_name for perfume_name, _ in similarities if perfume_name != name][:5]

    return top_similar

#각 향수에 대한 가장 유사한 향수들을 저장할 데이터프레임을 생성
similar_perfumes = []

for perfume in perfume_data['Name']:
    #각 향수에 대한 가장 유사한 향수들을 가져오기
    most_similar = get_most_similar_perfume(perfume, perfume_data)
    similar_perfumes.append({'Perfume': perfume, 'Similar Perfumes': ', '.join(most_similar)})

#리스트를 데이터프레임으로 변환
similar_perfumes_df = pd.DataFrame(similar_perfumes)

#데이터프레임을 CSV 파일로 저장
similar_perfumes_df.to_csv('data/similar_perfumes_data.csv', index=False)
