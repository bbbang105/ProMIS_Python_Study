#랜덤으로 달 입력받기
import random
num=random.randint(1,12)

while True:
    ans = str(input('Q. {}월은 며칠까지 있을까요?:'.format(num)))#사용자 입력
    if num in [1,3,5,7,8,10,12]:#31일까지 있는 경우
        if ans=='31':
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 31일입니다..')
    if num in [4,6,9,11]:#30일까지 있는 경우
        if ans=='30':
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 30일입니다..')
    if num==2:
        if ans=='28': #28일까지 있는 경우
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 28일입니다..')
    game=str(input('계속 하시겠습니까? (Y/N): '))#게임 반복 여부
    if game=='Y':
        num=random.randint(1,12)
        continue
    elif game=='N':
        print('게임을 종료합니다:)')
        break

        
