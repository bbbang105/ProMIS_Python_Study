import random

while True:
    n = random.randint(1,12)
    print("Q. {}월은 며칠까지 있을까요?".format(n))

    user = int(input("A."))

    if user == 30:
        if n in [4,6,9,11]:
            print("정답입니다!")
        else:
            print("틀렸습니다.")
        
    elif user == 31:
        if n in [1,3,5,7,8,10,12]:
            print("정답입니다!")
        else:
            print("틀렸습니다.")
    elif user == 28:
        if n ==2:
            print("정답입니다!")
        else:
            print("틀렸습니다.")
    else:
        print("틀렸습니다.")

    retry = input("계속 하시겠습니까? (Y/N)")
    if retry == "y":
        continue
    else:
        print("게임을 종료합니다:)")
        break
