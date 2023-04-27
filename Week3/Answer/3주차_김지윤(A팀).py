import random

#while 반복문으로 정답과 오답 가려내기
while True:
    month = random.randint(1,12) # 랜덤 달 범위 설정
    answer = 0 # answer값 초기화
    user = int(input('{}월은 며칠까지 있을까요?'.format(month)))
    if month in [1,3,5,7,8,10,12]:
        answer = 31
    elif month in [4,6,8,9,11]:
        answer = 30
    else:
        answer = 28
    if user == answer:
        print("정답입니다")
    else:
        print("틀렸습니다.. 정답은 {}일입니다.".format(answer))
        
    again = input("계속 하시겠습니까?(Y/N)")
    if again[0].lower() == 'y':
        continue
    else:
        break
    
