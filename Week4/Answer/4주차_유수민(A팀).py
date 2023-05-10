import random

n1 = random.randint(1,99)
n2 = random.randint(1,99)
#print(n1,n2)

user1 = int(input("첫 번째 숫자를 맞추세요."))
user2 = int(input("두 번째 숫자를 맞추세요."))

count =1


while True:
    
    #둘 다 맞추지 못한 경우
    if user1 != n1 and user2 != n2:
        print("아직 하나의 숫자도 맞추지 못했습니다..")
        while True:

            #시도한 횟수
            count += 1
            
            #첫 번째 숫자 게임 진행
            user1 = int(input("첫 번째 숫자를 맞추세요."))
            if user1 > n1:
                print("Down!")
                continue
            elif user1 < n1:
                print("Up!")
                continue
            else:
                print("첫 번째 숫자를 맞추셨습니다!")
                
                #두 번째 숫자 게임 진행
                while True:
                    count += 1

                    user2 = int(input("두 번째 숫자를 맞추세요."))
                    if user2 > n2:
                        print("Down!")
                        continue
                    elif user2 < n2:
                        print("Up!")
                        continue
                    else:
                        ("두 번째 숫자를 맞추셨습니다!")
                        break
                    
                break
                

    #첫 번째 숫자만 맞춘 경우
    elif user1 == n1 and user2 != n2:
        print("첫 번째 숫자는 이미 맞추셨습니다! 두 번째 숫자만 맞춰주시면 됩니다.")
        while True:
            
            count += 1

            #두 번째 숫자 게임 진행
            user2 = int(input("두 번째 숫자를 맞추세요."))
            if user2 > n2:
                print("Down!")
                continue
            elif user2 < n2:
                print("Up!")
                continue
            else:
                break
                
    #두 번째 숫자만 맞춘 경우
    elif user1 != n1 and user2 == n2:
        print("두 번째 숫자는 이미 맞추셨습니다! 첫 번째 숫자만 맞춰주시면 됩니다.")
        while True:
            
            count += 1
            
            #첫 번째 숫자 게임 진행
            user1 = int(input("첫 번째 숫자를 맞추세요."))
            if user1 > n1:
                print("Down!")
                continue
            elif user1 < n1:
                print("Up!")
                continue
            else:
                break
            
    #모두 맞춘 경우    
    else:
        print("두 숫자를 모두 맞추셨습니다!")

    print("축하드립니다! %d번 만에 정답을 맞추셨습니다!" %count)

    #게임 계속할지 여부
    retry = input("게임을 계속 진행하시겠습니까?[y/n]")
    if retry[0]=="y":
        n1 = random.randint(1,99)
        n2 = random.randint(1,99)

        user1 = int(input("첫 번째 숫자를 맞추세요."))
        user2 = int(input("두 번째 숫자를 맞추세요."))
        #print(n1, n2)

        count = 1
        continue
    else:
        print("게임을 종료합니다 :)")
        break

