#user_input == 2
from keras.preprocessing.text import text_to_word_sequence
from difflib import SequenceMatcher
import wishlist



class Notes:
    import pandas as pd
    from keras.preprocessing.text import text_to_word_sequence
    
    

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
        notes_input = input("Please enter Notes, separating words with a comma. : ")
        notes.append(notes_input)
        while True:
            more_notes = input("Would you like to enter more? [y/n]")
            if more_notes == 'y':
                notes_input = input("Please enter Notes, separating words with a comma. : ")
                notes.append(notes_input)
                continue
            elif more_notes == "n":
                #입력된 모든 노트를 하나의 문자열로 합치기
                all_notes = ', '.join(notes)
                #텍스트를 단어 시퀀스로 변환
                user_notes_sequence = Notes.text_to_word_sequence(all_notes)
                #유사한 향수 상위 1개 찾아서 출력
                most_similar = self.most_similar_notes(user_notes_sequence, self.perfume_data, 1)
                print("Most similar perfume : ", most_similar[0])

                more_notes = input("""
    Enter the number you want
    1. Save to Wishlist
    2. More recommendation
    3. Exiting the program
    """)
                if more_notes == "1" :
                    wishlist_data = wishlist.load_wishlist_from_file()
                    wishlist.add_to_wishlist(wishlist_data, most_similar[0] )
                    wishlist.save_wishlist_to_file(wishlist_data)
                    print(f"The perfume {most_similar[0]} has been added to the wishlist.")
                    break
                elif more_notes == "2" :
                    additional_similar = self.most_similar_notes(user_notes_sequence, self.perfume_data, 5)
                    selected_similar_perfumes = additional_similar[1:]
                    print("Additional recommended perfumes : ", selected_similar_perfumes)  # 첫 번째 추천을 제외하고 출력
                    notes_more_input = input("""
    Enter the number you want
    1. Save to Wishlist
    2. Exiting the program
    """)
                    if notes_more_input == "1" :
                        wishlist_data = wishlist.load_wishlist_from_file()
                        for perfume in selected_similar_perfumes:
                            wishlist.add_to_wishlist(wishlist_data, perfume)
                        wishlist.save_wishlist_to_file(wishlist_data)
                        print(f"The perfume {selected_similar_perfumes} has been added to the wishlist.")
                        break
                    elif notes_more_input == "2" :
                        print("Exiting the program.")
                        break
                        
                elif more_notes == "3" : #프로그램 종료
                    print("Exiting the program.")
                    break
                    
            else:
                print("Invalid input. Please try again. : ")





class Description:
    from difflib import SequenceMatcher
    import pandas as pd
    from keras.preprocessing.text import text_to_word_sequence
    

    #데이터 불러오기
    file_path = 'data/perfume_data_new.csv'
    perfume_data = pd.read_csv(file_path)

    #결측치 있다면 제거
    perfume_data = perfume_data.dropna(subset=['Description'])

    #각 향수의 'Description'과 사용자가 입력한 'description_input'의 유사도 계산하는 함수
    def description_similarity(self, str1, str2) :
      matcher = SequenceMatcher(None, str1, str2)
      similarity_ratio = matcher.ratio()
      return similarity_ratio


    #가장 유사도가 높은 'Description'의 향수를 찾는 함수
    def most_similar_description(self, user_description, df, num_result=5) :
      similarity = df['Description'].apply(lambda x: self.description_similarity(user_description, x))
      df['Similarity'] = similarity
      #most_similar_des = df.nlargest(num_result, 'Similarity')['Description'].tolist()
      most_similar_des = df.nlargest(num_result, 'Similarity')[['Name', 'Similarity']]  
      #'Name'과 'Similarity' 컬럼 포함
      return most_similar_des


    #사용자에게 'description_input' 입력받기
    def description_perfume(self):
      description = []
      description_input = input("Please enter the Description, separating words with spaces. : ")
      description.append(description_input)
      while True :
        more_description = input("Would you like to enter more? [y/n]")
        if more_description == 'y' :
            description_input = input("Please enter the Description, separating words with spaces. : ")
            description.append(description_input)
            continue
        elif more_description == "n" :
            #입력된 모든 노트를 하나의 문자열로 합치기
            all_description = ', '.join(description)
            most_similar_des = self.most_similar_description(all_description, self.perfume_data, 1)
            #유사한 향수 상위 1개 찾아서 출력
            #print("가장 유사한 향수:", most_similar_des[0])
            print("Most similar perfume : ", most_similar_des['Name'].iloc[0])  #'Name' 컬럼의 첫 번째 값 출력


            more_description = input("""
    Enter the number you want
    1. Save to Wishlist
    2. More recommendation
    3. Exiting the program
    """)
            if more_description == "1" :
                wishlist_data = wishlist.load_wishlist_from_file()
                wishlist.add_to_wishlist(wishlist_data, most_similar_des['Name'].iloc[0] )
                wishlist.save_wishlist_to_file(wishlist_data)
                print(f"The perfume {most_similar_des['Name'].iloc[0]} has been added to the wishlist.")
                break
            elif more_description == "2" :
                additional_similar = self.most_similar_description(all_description, self.perfume_data, 5)
                selected_similar_perfumes2 = additional_similar['Name'][1:].tolist()
                print("Additional recommended perfumes : ", selected_similar_perfumes2)
                description_more_input = input("""
    Enter the number you want
    1. Save to Wishlist
    2. Exiting the program
    """)
                if description_more_input == "1" :
                    wishlist_data = wishlist.load_wishlist_from_file()
                    for perfume in selected_similar_perfumes2 :
                            wishlist.add_to_wishlist(wishlist_data, perfume)
                    wishlist.save_wishlist_to_file(wishlist_data)
                    print(f"The perfume {selected_similar_perfumes2} has been added to the wishlist.")
                    break
                elif description_more_input == "2" :
                    print("Exiting the program.")
                    break
            elif more_description == "3" : #프로그램 종료
                print("Exiting the program.")
                break
        else:
          print("Invalid input. Please try again. : ")