

import random
num1= random.randint(1,99)
num2= random.randint(1,99)
a=0
b=0
i=0

while True:
   
    #둘 다 맞추지 못한 경우
    if a!=num1 and b!=num2:
        i+=1

        a=int(input('첫번째 숫자를 맞춰보세요:'))
        if a>num1:
            print('1st num Down!')
        else:
            print('1st num Up!')
            
        b=int(input('두번째 숫자를 맞춰보세요:'))   
        if b>num2:
            print('2nd num Down!')
        else:
            print('2nd num Up!')

        print('아직 하나의 숫자도 맞추지 못하셨습니다.')
        
        while True:
            i+=1
            a=int(input('첫번째 숫자를 맞춰보세요:'))
            if a>num1:
                print('1st num Down!')
        
            elif a<num1:
                print('1st num Up!')
        
            else:
                print('첫번째 숫자를 맞추셨습니다.')
            
            b=int(input('두번째 숫자를 맞춰보세요:'))
            if b>num2:
                print('2nd num Down!')
            elif b<num2:
                print('2nd num Up!')
            else:
                print('두번째 숫자를 맞추셨습니다.')
                break
        
    #첫번째 숫자만 맞춘 경우
    elif a==num1 and b!=num2:
        i+=1
        print('첫번째 숫자는 이미 맞추셨습니다. 두번째 숫자만 맞춰주시면 됩니다.')

        while True:
            i+=1
            b=int(input('두번째 숫자를 맞춰보세요:'))
            if b>num2:
                print('2nd num Down!')
            elif b<num2:
                print('2nd num Up!')
            else:
                print('두번째 숫자를 맞추셨습니다.')
                break
        

    
    #두번째 숫자만 맞춘 경우
    elif a!=num1 and b==num2:
        i+=1
        print('두번째 숫자는 이미 맞추셨습니다. 첫번째 숫자만 맞춰주시면 됩니다.')

        while True:
            i+=1
            a=int(input('첫번째 숫자를 맞춰보세요:'))
            if a>num1:
                print('1st num Down!')
            elif a<num1:
                print('1st num Up!')
            else:
                print('첫번째 숫자를 맞추셨습니다.')
                break

    else:#모두 맞춤
        i+=1
        break

print('축하드립니다.',i,'번만에 정답을 맞추셨습니다.')
print('게임을 종료합니다.')
    
        
