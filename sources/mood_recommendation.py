#user_input == 3
import pandas as pd
import random
import wishlist

def mood_recommendation(input_mood) :
    file_path = 'data/mood_perfumes_data.csv' 
    mood_perfume_data = pd.read_csv(file_path)

    filtered_perfumes = mood_perfume_data[mood_perfume_data['Emotion'] == input_mood]
    if not filtered_perfumes.empty :
        recommended_perfume = random.choice(filtered_perfumes['Name'].tolist())
        print(recommended_perfume) #입력한 감정에 맞는 향수 중 랜덤하게 하나 출력
        more_help1 = input("""Enter the number you want
            1. Save to Wishlist
            2. More recommendation
            3. Exiting the program
            """)
        if more_help1 == "1" : #위시리스트에 저장
            wishlist_data = wishlist.load_wishlist_from_file()
            wishlist.add_to_wishlist(wishlist_data, recommended_perfume )
            wishlist.save_wishlist_to_file(wishlist_data)
            print(f"The perfume {recommended_perfume} has been added to the wishlist.")
        elif more_help1 == "2" :
            print("<More Recommendation>")
            remaining_perfumes = filtered_perfumes[filtered_perfumes['Name'] != recommended_perfume] #현재 추천된 향수 제외
            more_recommendations = remaining_perfumes.sample(min(4, len(remaining_perfumes))) #남은 향수들 중 4개 랜덤하게 선택
            more_mood_perfume = []
            for perfume in more_recommendations['Name']: #추천된 향수들 출력
                print(perfume)
                more_mood_perfume.append(perfume)
            notes_more_input = input("""
    Enter the number you want
    1. Save to Wishlist
    2. Exiting the program
    """)
            if notes_more_input == "1" :
                wishlist_data = wishlist.load_wishlist_from_file()
                for perfume in more_mood_perfume:
                    wishlist.add_to_wishlist(wishlist_data, perfume)
                wishlist.save_wishlist_to_file(wishlist_data)
                print(f"The perfume {more_mood_perfume} has been added to the wishlist.")
            elif notes_more_input == "2" :
                print("Exiting the program.")
                return
        elif more_help1 == "3" : #프로그램 종료
            print("Exiting the program.")
            return
    
    else :
        print("No perfumes found for this emotion.")
        print("Existing the program.")
        return
        


