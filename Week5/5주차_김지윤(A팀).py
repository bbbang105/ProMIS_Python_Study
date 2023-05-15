elevator = ['시운', '다현', '현제', '유승', '혜원', '후동']

import random
location = random.randint(0,7)

elevator.insert(location,'상호')
a = 1

for i in elevator:
    if elevator[-1] == '상호':
        print('{}님이 {}층에서 하차하셨습니다'.format(elevator[-1],1+a))
        elevator.pop()
        print("현재 엘리베이터: ",elevator)
        print("상호님이 무사히 출근을 완료하였습니다.")
        break
    print('{}님이 {}층에서 하차하셨습니다'.format(elevator[-1],1+a))
    elevator.pop()
    print("현재 엘리베이터: ",elevator)
    a +=1
    
    
    
