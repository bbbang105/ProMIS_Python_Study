elevator = ['시운','다현','현제','유승','혜원','후동']
import random
location = random.randint(0,7)

elevator.insert(location,'상호')
floor = 2

while True:
    out = elevator.pop()
    print("{}님이 {}층에서 하차하셨습니다.".format(out,floor))
    print("현재 엘리베이터: {}".format(elevator))
    floor+=1
    if out=='상호':
        print("상호님이 무사히 출근을 완료하였습니다!")
        break
    
