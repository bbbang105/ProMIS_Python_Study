import random

# 30일, 31일 달 별로 리스트 만듦

list_30 = [4,6,9,11]
list_31 = [1,3,5,7,8,10,12]

while True:
    #문제를 낼 달을 선정
    n= random.randint(1,12)

    print("Q. %d월은 며칠까지 있을까요?" %n)

    user = int(input("A."))

    if n in list_30:
        if user == 30:
            print("정답입니다!")
        else:
            print("틀렸습니다.")    # 멘토: 틀렸을 때 정답을 출력해주는 부분이 빠졌네요!
                                   # 그래도 리스트 구분, 포멧팅 아주 잘하셨습니다 :)
    elif n in list_31:
        if user == 31:
            print("정답입니다!")
        else:
            print("틀렸습니다.") 
    else:
        # 2월
        if user == 28:
            print("정답입니다!")
        else:
            print("틀렸습니다.")
            
    # 사용자로부터 게임을 계속할지 or 종료할지 여부를 입력
    retry = input("계속 하시겠습니까? (Y/N)")
    if retry[0].lower() == "y":
        continue
    else:
        print("게임을 종료합니다:)")
        break
