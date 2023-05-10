import random
#랜덤 수 2개 배
num1 = random.randint(1,100)
num2 = random.randint(1,100)
count = 1
firstnum = int(input("첫번째 숫자를 맞춰보세요: "))
secondnum = int(input("두번째 숫자를 맞춰보세요: "))

while True:
    #둘 다 맞추지 못한 경우
    if firstnum != num1 and secondnum != num2:
        print("아직 하나의 숫자도 맞추지 못하셨습니다..")
        while True:
            # 첫번째 숫자 다시 맞추기
            firstnum = int(input("첫번째 숫자를 맞춰보세요: "))
            count += 1
            if firstnum > num1:
                print("Down!")
            elif firstnum < num1:
                print("Up!")
            else:
                print("첫번째 숫자를 맞추셨습니다!")
                break

            # 두번째 숫자 다시 맞추기
           
            secondnum = int(input("두번째 숫자를 맞춰보세요: "))
            count += 1
            if secondnum > num2:
                print("Down!")
            elif secondnum < num2:
                print("Up!")
            else:
                print("두번째 숫자를 맞추셨습니다!")
                break
            
           
                
            
    #첫번째 숫자만 맞춘 경우
    elif firstnum == num1 and secondnum != num2:
        print("첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞춰주시면 됩니다.")
        while True:
            #두번째 숫자 다시 맞추기
            secondnum = int(input("두번째 숫자를 맞춰주세요: "))
            count += 1
            if secondnum > num2:
                        print("Down!")
                        continue
            elif secondnum < num2:
                print("Up!")
                continue
            else:
                print("두번째 숫자를 맞추셨습니다!")
                break

    #두번째 숫자만 맞춘 경우
    elif firstnum != num1 and secondnum == num2:
        print("두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞춰주시면 됩니다.")
        while True:
            #첫번째 숫자 다시 맞추기
            firstnum = int(input("첫번째 숫자를 맞춰주세요: "))
            count += 1
            if firstnum > num1:
                print("Down!")
                continue
            elif firstnum < num1:
                print("Up!")
                continue
            else:
                print("첫번째 숫자를 맞추셨습니다!")
                break

    #모든 숫자를 맞춘 경우
    else:
        print("축하드립니다! {}번 만에 정답을 맞추셨습니다!".format(count))
        print("게임을 종료합니다 :)")
        break
        
        
    
