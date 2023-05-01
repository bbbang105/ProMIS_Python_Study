import random

while True:
    month = random.randint(1, 12)  # 랜덤으로 1월부터 12월까지 설정
    day = 0
    user = int(input('''Q. {}월은 며칠까지 있을까요?
A. '''.format(month)))
    if month in [2]:   # 28일까지인 경우
        day = 28
    elif month in [4,6,9,11]:    # 30일까지인 경우
        day = 30
    else:           # 31일까지인 경우
        day = 31
    if user == day:             # 정답인 경우
        print("정답입니다!")
    else:                       # 오답인 경우
        print('틀렸습니다.. 정답은 {}일입니다.'.format(day))

    # 사용자로부터 게임을 계속할지 여부를 입력받음.
    again = input("계속 하시겠습니까?(Y/N)")
    if again[0].upper() == 'Y':
        continue
    else:
        print("게임을 종료합니다:)")
        break
