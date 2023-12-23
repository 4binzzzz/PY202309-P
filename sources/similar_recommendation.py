#user_input == 1
from new_recommendation import *
import wishlist


#사용자가 입력한 향수가 데이터셋에 존재하는 경우
def similar_recommendation(input_name, df1) :
    similar_perfumes = df1[df1['Perfume'] == input_name]['Similar Perfumes'].values[0]
    similar_perfumes_list = similar_perfumes.split(', ')

    print("<Similar Perfume>")
    print('"',similar_perfumes_list[0],'"') #유사한 향수 1개 출력
    print()
    more_help = input("""Enter the number you want
        1. Save to Wishlist
        2. More recommendation
        3. Exiting the program
        """)
    if more_help == "1" : #위시리스트에 저장
        wishlist_data = wishlist.load_wishlist_from_file()
        wishlist.add_to_wishlist(wishlist_data, similar_perfumes_list[0])
        wishlist.save_wishlist_to_file(wishlist_data)
        print(f"The perfume {similar_perfumes_list[0]} has been added to the wishlist.")
    
    elif more_help == "2" :
        print("<More Recommendation>")
        selected_perfumes = [] #유사한 향수 4개 저장할 리스트
        for i in range(1, len(similar_perfumes_list)) : #유사한 향수 4개 더 출력
            print('"',similar_perfumes_list[i],'"')
            similar_perfume = similar_perfumes_list[i]
            selected_perfumes.append(similar_perfume)
        similar_more_input = input("""
    Enter the number you want
    1. Save to Wishlist
    2. Exiting the program
    """)
        if similar_more_input == "1" :
            wishlist_data = wishlist.load_wishlist_from_file()
            for perfume in selected_perfumes:
                wishlist.add_to_wishlist(wishlist_data, perfume)
            wishlist.save_wishlist_to_file(wishlist_data)
            print(f"The perfume {selected_perfumes} has been added to the wishlist.")
        elif similar_more_input == "2" :
            print("Exiting the program.")
            return
                    
    elif more_help == "3" : #프로그램 종료
        print("Exiting the program.")
        return


#사용자가 입력한 향수가 데이터셋에 존재하지 않는 경우
def no_similar_recommendation() :
    print("Sorry, Not Found.. :<")
    more_help = input("""1. Enter Notes to search Or 2. Exiting the program
Enter the number you want
""")
    if more_help == "1" :
        # Notes 클래스의 인스턴스 생성 및 메서드 호출
        notes_instance = Notes()
        similar_notes = notes_instance.notes_perfume()
        print(similar_notes)
    elif more_help == "2" :
        #return_to_menu()
        print("Exiting the program.")
        return
    


