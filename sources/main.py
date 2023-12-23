from similar_recommendation import *
from new_recommendation import *
from mood_recommendation import *
from wishlist import *

import pandas as pd


#위시리스트 파일 
wishlist_filename = "wishlist.txt"

#프로그램 시작 시 wishlist.txt 파일이 없으면 생성
if not os.path.exists(wishlist_filename):
    open(wishlist_filename, 'w').close()


dataFrame = pd.read_csv("data/perfume_data_new.csv")
df1 = pd.read_csv("data/similar_perfumes_data.csv")
df2 = pd.read_csv("data/mood_perfumes_data.csv")

#프로그램 첫 실행시 출력될 문구
print("******Perfume Recommendation System******")

def main_menu() : 
    user_input = input("""
Enter the number of the menu
1. Recommend a perfume similar to a previous one
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
                #Description 클래스의 인스턴스 생성 및 메서드 호출
                description_instance = Description()
                similar_description = description_instance.description_perfume()
                print(similar_description)
                break
            else :
                print("Invalid input. Please try again. : ")
        

    elif user_input == "3" :
        while True :
            input_mood = input("Enter your mood [happiness, sadness, anger, calmness, love] : ")
            mood_list = ['happiness', 'sadness', 'anger', 'calmness', 'love']
            if input_mood in mood_list : #감정 정확하게 입력한 경우
                mood_recommendation(input_mood)
                break
            else: #잘못입력한 경우
                print("Invalid input. Please enter again : ")

    elif user_input == "4" :
        wishlist = load_wishlist_from_file()
        display_wishlist(wishlist) #위시리스트 출력
        
        while True:
            choice = input("\nChoose an option:\n1. Add to wishlist\n2. Delete from wishlist\n3. Exit Program\n")
            
            if choice == "1":
                perfume_name = input("Enter the name of the perfume to add: ")
                print('')
                add_to_wishlist(wishlist, perfume_name)
                save_wishlist_to_file(wishlist)
                display_wishlist(wishlist)

            elif choice == "2":
                delete_number = input("Enter the number of the perfume to delete: ")
                print('')
                if delete_number.isdigit() and 0 < int(delete_number) <= len(wishlist):
                    delete_from_wishlist(wishlist, int(delete_number))
                    save_wishlist_to_file(wishlist)
                    display_wishlist(wishlist)
                else:
                    print("Invalid number. Please try again.")

            elif choice == "3":
                print("Exiting the program.")
                return
            
            else:
                print("Invalid input. Please try again. : ")
        

    elif user_input == "5" :
        print("Exiting the program.")
        return
    
    else :
        print("Invalid input. Please try again. : ")


if __name__ == "__main__":
    main_menu()
    