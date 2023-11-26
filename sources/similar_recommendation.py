#user_input == 1
from new_recommendation import *
from wishlist import *

from middle import call_main_menu

#main.py의 메인 메뉴 호출을 위한 함수
def return_to_menu():
    call_main_menu()

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
        3. Return to menu
        """)
    if more_help == "1" : #위시리스트에 저장
        pass #wishlist.py의 위시리스트 관련 모듈 불러오기
    elif more_help == "2" :
        print("<More Recommendation>")
        for i in range(1, len(similar_perfumes_list)) : #유사한 향수 4개 더 출력
            print('"',similar_perfumes_list[i],'"')
    elif more_help == "3" : #초기 메뉴로 돌아가기
        return_to_menu()


#사용자가 입력한 향수가 데이터셋에 존재하지 않는 경우
def no_similar_recommendation() :
    print("Sorry, Not Found.. :<")
    more_help = input("""1. Enter Notes to search Or 2. Return to menu
Enter the number you want
""")
    if more_help == "1" :
        # Notes 클래스의 인스턴스 생성 및 메서드 호출
        notes_instance = Notes()
        similar_notes = notes_instance.notes_perfume()
        print(similar_notes)
    elif more_help == "2" :
        return_to_menu()
    


