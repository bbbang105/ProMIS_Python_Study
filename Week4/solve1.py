import random                 # 랜덤 모듈 import

num1 = random.randint(1,100)  # Up-Down Game을 진행할 숫자1
num2 = random.randint(1,100)  # Up-Down Game을 진행할 숫자2 
temp1 = False                 # 숫자1을 맞췄는지의 유무 확인
temp2 = False                 # 숫자2를 맞췄는지의 유무 확인
cnt = 0                       # 시도한 횟수 

# <Up-Down Game 실행>
while True:
    # <1. 숫자를 둘 다 못 맞춘 상태>
    if not temp1 and not temp2:
        print('아직 하나의 숫자도 맞추지 못하셨습니다..')  # 안내문 출력
        cnt += 1                                        # 횟수 +1
        # <1-1. 첫번째 숫자 맞추기>
        answer1 = int(input('첫번째 숫자를 맞춰보세요: '))
        if num1 > answer1:
            print('Up!')
        elif num1 < answer1:
            print('Down!')
        else:                                           # 정답을 맞출 경우
            print('첫번째 숫자를 맞추셨습니다!')
            temp1 = True                                # 첫번째 숫자를 맞춘 상태로 변경
            
        # <1-2. 두번째 숫자 맞추기>
        answer2 = int(input('두번째 숫자를 맞춰보세요: '))
        if num2 > answer2:
            print('Up!')
        elif num2 < answer2:
            print('Down!')
        else:                                           # 정답을 맞출 경우
            print('두번째 숫자를 맞추셨습니다!')    
            temp2 = True                                # 두번째 숫자를 맞춘 상태로 변경
            
    # <2. 첫번째 숫자만 맞춘 상태>
    elif temp1 and not temp2:
        print('첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞춰주시면 됩니다.')  # 안내문 출력
        cnt += 1                                        # 횟수 +1
        # <2-1. 두번째 숫자 맞추기>
        answer2 = int(input('두번째 숫자를 맞춰보세요: '))
        if num2 > answer2:
            print('Up!')
        elif num2 < answer2:
            print('Down!')
        else:                                           # 정답을 맞출 경우
            print('두번째 숫자를 맞추셨습니다!')    
            temp2 = True                                # 두번째 숫자를 맞춘 상태로 변경
            
    # <3. 두번째 숫자만 맞춘 상태>
    elif not temp1 and temp2:
        print('두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞춰주시면 됩니다.')  # 안내문 출력
        cnt += 1                                        # 횟수 +1
        # <3-1. 첫번째 숫자 맞추기>
        answer1 = int(input('첫번째 숫자를 맞춰보세요: '))
        if num1 > answer1:
            print('Up!')
        elif num1 < answer1:
            print('Down!')
        else:                                           # 정답을 맞출 경우
            print('첫번째 숫자를 맞추셨습니다!')    
            temp1 = True                                # 첫번째 숫자를 맞춘 상태로 변경
            
    # <4. 숫자를 모두 맞춘 상태>
    if temp1 and temp2:
        print(f'축하드립니다! {cnt}번 만에 정답을 맞추셨습니다!')
        print('게임을 종료합니다 :)')
        break