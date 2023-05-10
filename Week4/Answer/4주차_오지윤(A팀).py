import random
num1=random.randint(1,100)
num2=random.randint(1,100)
ans1 = 0
ans2 = 0

count = 0

while True:
    if ans1!=num1 and ans2!=num2:
        print("아직 하나의 숫자도 맞추지 못하셨습니다..")
    if ans1!=num1:
        ans1=int(input("첫 번째 숫자를 맞춰보세요: "))
        if num1<ans1:
            print('Down!')
        if num1>ans1:
            print('Up!')
    if ans2!=num2:
        ans2=int(input("두 번째 숫자를 맞춰보세요: "))
        if num2<ans2:
            print('Down!')
        if num2>ans2:
            print('Up!')
    count+=1
    if ans1==num1 and ans2==num2:
        print("축하드립니다!", count, "번 만에 맞추셨습니다!")
        break
    if ans1==num1:
        print("첫번째 숫자는 이미 맞추셨습니다! 두번째 숫자만 맞춰주시면 됩니다")
        continue
    if ans2==num2:
        print("두번째 숫자는 이미 맞추셨습니다! 첫번째 숫자만 맞춰주시면 됩니다")
        continue
