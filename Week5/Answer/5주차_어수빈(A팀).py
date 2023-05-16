import random
location = random.randint(0,7)

elevator = ['시운', '다현', '현제', '유승', '혜원', '후동']
elevator.insert(location,'상호')
reversed_add=list(reversed(elevator))
floor=2

for a in reversed_add:
    print('{}님이 {}층에서 하차하셨습니다.'.format(a,floor))
    floor+=1

    if a=='상호':
        print('상호님이 무사히 출근을 완료하였습니다!')
        break
    
    
