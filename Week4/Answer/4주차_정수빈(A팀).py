import random

num1 = random.randint(1,100)
num2 = random.randint(1,100)

count=0

while True:
    a = int(input("첫번째 숫자를 맞춰보세요: "))
    count+=1
   
    if num1<a:
        print("Down!")
    elif num1>a:
        print("Up!")
    else:
        print("첫번째 숫자를 맞추셨습니다!")
        
        
    b=int(input("두번째 숫자를 맞춰보세요: "))
    if num2<b:
        print("Down!")
    elif num2>b:
        print("Up!")
    else:
        print("두번째  숫자를 맞추셨습니다!")


    if a==num1 and b==num2:
        print("축하드립니다!",count,"번 만에 정답을 맞추셨습니다!")
        print("게임을 종료합니다:)")
        break
    elif a!=num1 and b!=num2:
        print("아직 하나의 숫자도 맞추지 못하셨습니다.")

        
    elif a!=num1 and b==num2:
        a=print("두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞춰주시면 됩니다.")
       
    elif a==num1 and b!=num2:
        print("첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞춰주시면 됩니다.")
        #둘 중 하나의 숫자를 맞추면 '첫번째 숫자는~됩니다' 부분이 반복되서 출력되고 두번째 숫자만 입력할 수 있도록 해야 하는데 모르겠습니다ㅠㅠ

