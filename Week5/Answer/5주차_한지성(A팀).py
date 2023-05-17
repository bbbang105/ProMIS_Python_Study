import random
elevator = ['시운', '다현', '현제', '유승', '혜원', '후동']
location = random.randrange(1,6)
elevator.insert(location, '상호')
print('현재 엘리베이터 : {}'.format(elevator))
i=1
for x in elevator:
    print('{}님이 {}층에서 하차하셨습니다.'.format(elevator[7-i], i+1))
    if elevator.pop(7-i)=='상호':
          break
    print('현재 엘리베이터 : {}'.format(elevator))
    i+=1
print('상호님이 무사히 출근을 완료하였습니다!')
exit()

