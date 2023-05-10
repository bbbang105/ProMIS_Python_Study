import random

num1 = random.randint(1,99)
num2 = random.randint(1,99)
#print(num1, num2)

user1 = int(input("첫 번째 숫자를 맞히세요."))
user2 = int(input("두 번째 숫자를 맞히세요."))


count = 0


while True:
    count += 1
    
    if num1 != user1 and num2 != user2:
        print("아직 하나의 숫자도 맞히지 못하셨습니다..")

        user1 = int(input("첫 번째 숫자를 맞히세요:"))
        if user1 > num1:
            print("Down!")
        elif user1 < num1:
            print("Up!")
        else:
            print("정답입니다!")
  
        user2 = int(input("두 번째 숫자를 맞히세요:"))
        if user2 > num2:
            print("Down!")
        elif user2 < num2:
            print("Up!")
        else:
            print("정답입니다!")
        continue
        
    elif num1 == user1 and num2 != user2:
        print("첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞혀주시면 됩니다.")

        user2 = int(input("두 번째 숫자를 맞히세요:"))
        if user2 > num2:
            print("Down!")
        elif user2 < num2:
            print("Up!")
        else:
            print("정답입니다!")
        continue
    
    elif num1 != user1 and num2 == user2:
        print("두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞혀주시면 됩니다.")

        user1 = int(input("첫 번째 숫자를 맞히세요:"))
        if user1 > num1:
            print("Down!")
        elif user1 < num1:
            print("Up!")
        else:
            print("정답입니다!")
    
    else:
        break
    
print("축하합니다. %d번 만에 맞히셨습니다!" %count)
print("게임을 종료합니다:)")
        

        
        
            
            
