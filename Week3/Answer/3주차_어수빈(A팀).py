
#sol1)숫자 범위로 지정
import random

while True:
    num= random.randint(1,12)

    a=int(input('Q.'+ str(num) +'월은 며칠까지 있을까요?'))

    if num==2:
        if a==28:
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 28일 입니다.')
        

    elif (num%2!=0 and num<8) or (num%2==0 and num>=8) :
        if a==31:
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 31일 입니다.')

    else:
        if a==num:  # 멘토: num을 30으로 수정하셔야 할 것 같아요!
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 30일 입니다.')
            
    b=input('계속 하시겠습니까?(Y/N)')
    bu=b.upper()
    if bu=='Y':
        continue
    
    if bu=='N':
        print('게임을 종료합니다.')
        break

#sol2)리스트 사용
import random
mon30=[4,6,9,11]
mon31=[1,3,5,7,8,10,12]

while True:
    num= random.randint(1,12)

    a=int(input('Q.'+ str(num) +'월은 며칠까지 있을까요?'))

    if num==2:
        if a==28:
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 28일 입니다.')
        

    elif num in mon31 :
        if a==31:
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 31일 입니다.')

    else:           # 멘토: 여기도 num을 30으로 수정하셔야 할 것 같아요.
        if a==num:  # 두 가지 방법으로 하신 점 너무 잘하셨고, 고생하셨습니다 :)
              print('정답입니다!')

        else:
            print('틀렸습니다. 정답은 30일 입니다.')
            
    b=input('계속 하시겠습니까?')
    bu=b.upper()
    if bu[0]=='Y':
        continue
    if bu[0]=='N':
        print('게임을 종료합니다.')
        break

    


        
            
