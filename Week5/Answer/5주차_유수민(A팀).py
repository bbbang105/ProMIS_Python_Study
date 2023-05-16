elevator = ['시운', '다현', '현제', '유승', '혜원', '후동']


import random
location = random.randint(0,7)

elevator.insert(location, '상호')

floor = 2
for i in elevator:
    print("{}님이 {}층에서 하차하셨습니다.".format(elevator[-1],floor))
    elevator.pop()
    print("현재 엘리베이터:",elevator)
    floor+=1

    if not "상호" in elevator:
        print("상호님이 무사히 출근을 완료하였습니다!")
        break
    
