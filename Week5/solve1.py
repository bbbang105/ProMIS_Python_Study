import random

elevator = ['시운', '다현', '현제', '유승', '혜원', '후동'] # 이미 탑승해 있는 인턴 6명

location = random.randint(0,7)          # 들어갈 위치를 설정
elevator.insert(location, '상호')       # 해당 위치에 넣어줌

for floor in range(2,len(elevator)+2):  # 2층부터 8층까지 반복 설정
    people = elevator.pop()             # pop()을 사용하여 하차할 사람을 리스트에서 꺼냄
    print(f'{people}님이 {floor}층에서 하차하셨습니다.')
    print(f'현재 엘리베이터: {elevator}')
    
    if people == '상호':                # 상호가 하차했을 경우
        print('상호님이 무사히 출근을 완료하였습니다!')
        break