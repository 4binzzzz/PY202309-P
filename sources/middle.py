from main import main_menu

#중간 모듈을 통한 간접 호출
#순환 참조를 위해 새로 생성한 함수
def call_main_menu():
    main_menu()