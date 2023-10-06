


# 사람들끼리 아래 코드가 무엇인지 알아볼 수 있도록 정보 제공

# 리스트에 저장하기 위해 리스트 설정
results = []

# 리스트 조회
number = [[1,2,3],[4,5,6],[7,8,9]]

# 짝수인지 아닌지 판별
for i in number:
    for number in i:
        if number % 2 == 0:
# 짝수이면 결과 값을 리스트에 저장
            results.append(number)

# 결과값 출력
print(results)





# 탁구대회 참가인원
PPname = ["나영", "예진", "원빈", "현빈"]

# 최종 저장 위치
results = []

# 메일 내용 만드는 함수
def create_contents_of_mail(XX):
    mail = "안녕하세요." + XX + "님, 한국교통대학교 천하제일 탁구대회에 참여해주셔서 감사합니다. 행사 일시 : 10:30 AM, 참여 부탁드립니다."
    return mail

# 함수 호출
for i in PPname:
    # print(i)
    print(create_contents_of_mail(i))

# 메일 내용 저장
results.append(create_contents_of_mail(i))

# 결과값 출력
print(results)
