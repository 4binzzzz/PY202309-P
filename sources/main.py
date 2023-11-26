from similar_recommendation import *
from new_recommendation import *
from mood_recommendation import *
from wishlist import *

import pandas as pd

dataFrame = pd.read_csv("data/perfume_data_new.csv")
df1 = pd.read_csv("data/similar_perfumes_data.csv")
#df2 = pd.read_csv("data/mood_perfumes_data.csv")

#프로그램 첫 실행시 출력될 문구
print("******Perfume Recommendation System******")

def main_menu() : 
    user_input = input("""
Enter the number of the menu
1. Recommend a product similar to what you used to do
2. Get a new perfume recommendation
3. Recommend a perfume according to your mood
4. Get a wish list file
5. Existing the program
""")

    if user_input == "1" :
        input_name = input("Enter a perfume name : ")
        if input_name in df1['Perfume'].values: #유저가 입력한 향수가 데이터셋에 존재하는 경우
            similar_recommendation(input_name, df1)
        else: #존재하지 않는 경우
            no_similar_recommendation()


    elif user_input == "2" :
        while True :
            input_option = input("""
You can search for similar perfumes by entering 1.Notes or 2.Description. 
Which one would you like to use for the search?
Enter the number you'd like to use. [1 or 2]
""")
            if input_option == "1" :
                #Notes 클래스의 인스턴스 생성 및 메서드 호출
                notes_instance = Notes()
                similar_notes = notes_instance.notes_perfume()
                print(similar_notes)
                break
            elif input_option == "2" :
                #description_perfume()
                break
            else :
                print("잘못된 입력입니다. 다시 입력하세요.")
        

    elif user_input == "3" :
        #mood_recommendation()
        pass

    elif user_input == "4" :
        #wishlist_file()
        pass

    elif user_input == "5" :
        print("Exiting the program.")
        return
    
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")


if __name__ == "__main__":
    main_menu()
    