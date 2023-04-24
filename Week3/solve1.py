import random

# 달 일수별로 구분
a = [1,3,5,7,8,10,12] # 31일까지 있는 달들
b = [4,6,9,11]        # 30일까지 있는 달들
c = [2]               # 28일까지 있는 달

# while반복문
while True:
    # 문제를 낼 달을 random으로 선정함
    month = random.randint(1,12)
    # random으로 나온 달에 맞는 일수를 answer에 넣어줌
    if month in a:
        answer = 31
    elif month in b:
        answer = 30
    else:
        answer = 28
        
    # 값을 입력받아 정답 or 오답을 파악
    print(f'Q. {month}월은 며칠까지 있을까요?')
    num = int(input('A. '))
    if num == answer:
        print('정답입니다!')
    else:
        print(f'틀렸습니다..정답은 {answer}일입니다..')
        
    # 게임을 계속할지 or 종료할지 선택
    temp = input('계속 하시겠습니까?(Y/N): ')
    if temp == 'Y':
        continue
    else:
        print('게임을 종료합니다:)')
        break