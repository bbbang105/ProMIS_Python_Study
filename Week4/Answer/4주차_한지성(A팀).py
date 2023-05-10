import random
num1 = int(random.random() * 100 % 100) # 난수 설정 
num2 = random.randrange(1,101) # 숫자를 무한정 선정하는 것보단 100까지로 한정하였습니다.

i=0
count = 0 # 시행 횟수 
situation = 1
while i == 0: # 저는 이 방법 외에 무한루프를 설정하는 방법을 모릅니다... 어떻게 했어야 할까요?
    if situation == 1: # 첫번째, 두번째 숫자 모두 맞추지 못한 상황
        answer = int(input('첫번째 숫자를 맞춰보세요 :'))
        if answer == num1:
            print('첫번째 숫자를 맞추셨습니다!')
            situation = 2
        elif answer > num1:
            print('Down!')
        else:
            print('Up!')
        answer = int(input('두번째 숫자를 맞춰보세요 :'))
        if answer == num2:
            print('두 번째 숫자를 맞추셨습니다!')
            situation = 3
        elif answer > num2:
            print('Down!')
            count+=1
        else:
            print('Up!')
            count+=1
        if situation == 1:
            print('아직 하나의 숫자도 맞추지 못하였습니다...')


    if situation == 2: #첫번째 숫자만 맞춘 상황
        print('첫번째 숫자는 이미 맞추셨습니다. 두번째 숫자만 맞춰주시면 됩니다.')
        answer = int(input('두번째 숫자를 맞춰보세요 :'))
        if answer == num2:
            print('두 번째 숫자를 맞추셨습니다!')
            situation = 4
        elif answer > num2:
            print('Down!')
            count+=1
        else:
            print('Up!')
            count+=1

    if situation == 3:
        print('두번째 숫자는 이미 맞추셨습니다. 첫번째 숫자만 맞춰주시면 됩니다.')
        answer = int(input('첫번째 숫자를 맞춰보세요 :'))
        if answer == num1:
            print('첫 번째 숫자를 맞추셨습니다!')
            situation = 4
        elif answer > num1:
            print('Down!')
            count+=1
        else:
            print('Up!')
            count+=1 
        
            

    if situation == 4: #첫번째, 두번째 숫자 모두 맞춘 상황
        count+=1
        print('두번째 숫자를 맞추셨습니다!')
        print('축하드립니다. {}번 만에 정답을 맞추셨습니다.'.format(count))
        print('게임을 종료합니다 :)')
        break

#질문 : 이번주 문제에 있어서의 제 풀이 전략은 상황을 네 가지로 나누는 것이었습니다.
#어쩌면 해당 접근하는 방식 자체가 비효율적일지도 모르겠습니다만...
#제가 체계적으로 공부를 한 게 아니라 개념들이 명확히 서 있는게 아니라서
#다소 감각적으로 온전히 감에 의존해 문제를 풀었습니다.
#그렇기에 현재 코드는 말 그대로 돌아만 갈 수 있도록,
#다소 무식하게 작성되었다고 생각합니다.
#코드에 있어서 피드백이나 코멘트 해주실 부분이 있으면 부탁드리겠습니다.
#감사합니다.
    



    
    
    
