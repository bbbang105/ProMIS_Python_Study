import random
# 숫자가 랜덤으로 나오는 방법
num1 = random.randint(1,100)
num2 = random.randint(1,100)
count = 0
user1 = int(input('첫번째 숫자를 맞춰보세요: '))
user2 = int(input('두번째 숫자를 맞춰보세요: '))

while True:
    # 입력한 수가 모두 틀린 경우
    if user1 != num1 and user2 != num2:
        print('아직 하나의 숫자도 맞추지 못하셨습니다..')
        while True:
            user1 = int(input('첫번째 숫자를 맞춰보세요: '))
            count += 1
            if user1 < num1:
                print('Up!')
            elif user1 > num1:
                print('Down!')
            else:
                print('첫번째 숫자를 맞추셨습니다.')
                break

            user2 = int(input('두번째 숫자를 맞춰보세요: '))
            count += 1
            if user2 < num2:
                print('Up!')
            elif user2 > num2:
                print('Down!')
            else:
                print('두번째 숫자를 맞추셨습니다.')
                break
    # 첫번째 수만 맞춘 경우
    elif user1 == num1 and user2 != num2:
        print('첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞춰주시면 됩니다.')
        while True:
            user2 = int(input('두번째 숫자를 맞춰주세요: '))
            count += 1
            if user2 < num2:
                print('Up!')
            elif user2 > num2:
                print('Down!')
            else:
                print('두번째 숫자를 맞추셨습니다.')
                break
    # 두번째 수만 맞춘 경우
    elif user1 != num1 and user2 == num2:
        print('두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞춰주시면 됩니다.')
        while True:
            user1 = int(input('첫번째 숫자를 맞춰주세요: '))
            count += 1
            if user1 < num1:
                print('Up!')
            elif user1 > num1:
                print('Down!')
            else:
                print('첫번째 숫자를 맞추셨습니다.')
                break
    # 모든 숫자를 맞춘 경우
    else:
        print('축하드립니다! {}번 만에 정답을 맞추셨습니다!'.format(count))
        print('게임을 종료합니다 :)')
        break
