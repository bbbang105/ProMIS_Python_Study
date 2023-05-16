ele = ['시운', '다현', '현제', '유승', '혜원', '후동']
import random
location = random.randint(0,7)
ele.insert(location, "상호")
i=1
while True:
    b=ele
    print(b[len(b)-i],"님이", i, "층에서 하차하셨습니다." )
    a=ele.pop()
    print("현재 엘리베이터 : ", a)
    i+=1
    if "상호" not in a:
        print("상호님이 무사히 출근을 완료하였습니다!")
        break
    
