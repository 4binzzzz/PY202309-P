#user_input == 2
from keras.preprocessing.text import text_to_word_sequence
from middle import call_main_menu

#main.py의 메인 메뉴 호출을 위한 함수
def return_to_menu():
    call_main_menu()

class Notes:
    import pandas as pd
    from keras.preprocessing.text import text_to_word_sequence
    from middle import call_main_menu
    
    #main.py의 메인 메뉴 호출을 위한 함수
    def return_to_menu():
        call_main_menu()

    # 데이터 불러오기
    file_path = 'data/perfume_data_new.csv'
    perfume_data = pd.read_csv(file_path)

    # 결측치 있는 행을 제거 (Notes 열에 대해 80개의 결측치 존재)
    perfume_data = perfume_data.dropna(subset=['Notes'])

    # 각 향수의 'Notes'를 단어 시퀀스로 변환하여 새로운 열에 저장
    perfume_data['NotesSequence'] = perfume_data['Notes'].apply(lambda x: text_to_word_sequence(x))

    # 단어 중복 유사도를 계산하는 함수
    def notes_overlap_similarity(notes_seq1, notes_seq2):
        set_1 = set(notes_seq1)
        set_2 = set(notes_seq2)
        return len(set_1.intersection(set_2))

    # 가장 유사한 향수를 찾는 함수
    def most_similar_notes(self, user_notes_seq, df, num_results=5):
        similarity = []
        for _, row in df.iterrows():
            similar = Notes.notes_overlap_similarity(user_notes_seq, row['NotesSequence'])
            similarity.append((row['Name'], similar))

        similarity = sorted(similarity, key=lambda x: x[1], reverse=True) #유사도를 기준으로 정렬
        return [perfume_name for perfume_name, _ in similarity][:num_results]

    def notes_perfume(self):
        notes = []
        notes_input = input("단어 사이에 ,을 넣어 Notes를 입력하세요. : ")
        notes.append(notes_input)
        while True:
            more_notes = input("더 입력하시겠어요? [y/n]")
            if more_notes == 'y':
                notes_input = input("단어 사이에 ,을 넣어 Notes를 입력하세요. : ")
                notes.append(notes_input)
                continue
            elif more_notes == "n":
                #입력된 모든 노트를 하나의 문자열로 합치기
                all_notes = ', '.join(notes)
                #텍스트를 단어 시퀀스로 변환
                user_notes_sequence = Notes.text_to_word_sequence(all_notes)
                #유사한 향수 상위 1개 찾아서 출력
                most_similar = self.most_similar_notes(user_notes_sequence, self.perfume_data, 1)
                print("가장 유사한 향수:", most_similar[0])

                more_notes = input("""
    Enter the number you want
    1. Save to Wishlist
    2. More recommendation
    3. Return to menu
    """)
                if more_notes == "1" :
                    pass #wishlist.py의 위시리스트 관련 모듈 불러오기
                elif more_notes == "2" :
                    additional_similar = self.most_similar_notes(user_notes_sequence, self.perfume_data, 5)
                    print("추가 추천 향수:", additional_similar[1:])  # 첫 번째 추천을 제외하고 출력
                    notes_more_input = input("""
    Enter the number you want
    1. Save to Wishlist
    2. Return to menu
    """)
                    if notes_more_input == "1" :
                        pass #wishlist.py의 위시리스트 관련 모듈 불러오기
                    elif notes_more_input == "2" :
                        return_to_menu()
                        break
                elif more_notes == "3" : #초기 메뉴로 돌아가기
                    return_to_menu()
                    break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")





'''
def description_perfume() :
    description = []
    description_input = input("향수에 대한 설명을 입력하세요. 단어 사이 띄어쓰기 필수 : ")
    while True :
        more_description = input("더 입력하시겠어요? [y/n]")
        if more_description == 'y' :
            description_input = input("단어 사이에 ,을 넣어 Description을 입력하세요. : ")
            description.append(description_input)
            continue
        elif more_description == "n" :
            ##################토큰화해서 유사한거 출력하는 함수 호출#####################
            ##################search engine 방법 사용#####################
            break
        else :
            print("잘못된 입력입니다. 다시 입력하세요.")
'''