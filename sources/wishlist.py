#user_input == 4

import os

wishlist_filename = "wishlist.txt"

def add_to_wishlist(wishlist, perfume_name):
    #위시리스트에 향수 추가
    wishlist.append(perfume_name)

def display_wishlist(wishlist):
    #위시리스트에 있는 모든 향수 표시
    if not wishlist:
        print("위시리스트가 비어 있습니다.")
    else:
        print("위시리스트:")
        for i in range(len(wishlist)) :
            perfume_name = wishlist[i]
            print(f"{i+1}. {perfume_name}")

def save_wishlist_to_file(wishlist):
    #위시리스트를 파일에 저장
    with open(wishlist_filename, 'w', encoding='utf-8') as write_fp:
        for perfume_name in wishlist:
            write_fp.write(perfume_name + "\n")


def load_wishlist_from_file():
    #위시리스트 파일 불러오기
    wishlist = []
    read_fp = open(wishlist_filename, 'r', encoding='utf-8')
    lines = read_fp.readlines()
    for line in lines :
        wishlist.append(line.strip())
    return wishlist

def delete_from_wishlist(wishlist, number):
    #위시리스트에서 특정 번호의 항목 삭제
    del wishlist[number - 1]
