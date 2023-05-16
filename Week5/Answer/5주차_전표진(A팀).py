elevator = ['시운', '다현', '현제', '유승', '혜원', '후동']


import random
location = random.randint(0,7)
elevator.insert(location,"상호")

a = 2
print(elevator)

for x in elevator:
    
    print("%s님이 %d층에서 하차하셨습니다," %(elevator[-1],a))
    elevator.pop()
    print("현재 엘리베이터:",elevator)
    a+=1

    if not "상호" in elevator:
        print("상호님이 무사히 출근을 완료하셨습니다!")
        break
