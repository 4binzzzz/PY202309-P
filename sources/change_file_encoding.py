import chardet

# 파일 경로
file_path = 'data/perfume_data.csv'

# 파일의 실제 인코딩 확인
with open(file_path, 'rb') as file:
    result = chardet.detect(file.read())

# 확인된 인코딩 출력
print(f"파일의 실제 인코딩: {result['encoding']}, 신뢰도: {result['confidence']}")

# 파일을 확인된 인코딩(Windows-1254)으로 읽어오기
with open(file_path, 'r', encoding=result['encoding'], errors='replace') as file:
    content = file.read()

# 새로운 파일이 저장될 경로 (UTF-8로 저장할 파일)
new_file_path = 'data/perfume_data_new.csv'


# 파일 내용을 'UTF-8'로 인코딩하여 저장
with open(new_file_path, 'w', encoding='utf-8') as file:
    file.write(content)
