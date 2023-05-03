#문제를 낼 달 입력받기
import random

while True:
    month=random.randint(1,12)
    a = int(input("Q. {}월은 며칠까지 있을까요?:".format(month)))#사용자로부터 답 입력
    if month in [1,3,5,7,8,10,12]:
        if a=="31":
            print("정답입니다!")
        else:
            print("틀렸습니다..정답은 31일입니다..")
    elif month in [4,6,9,11]:
        if a=="30":
            print("정답입니다!")
        else:
            print("틀렸습니다..정답은 30일입니다..")
    else :
        if a=="28": 
            print("정답입니다!")
        else:
            print("틀렸습니다..정답은 28일입니다..")
    b=input("계속 하시겠습니까? (Y/N): ")#문제 진행 여부 질문
    if b=="Y":
        continue
    elif b=="N":
        print("게임을 종료합니다:)")
        break
