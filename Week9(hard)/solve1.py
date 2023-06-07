import random

drink_num = 0                       # 술을 마신 횟수
while True:
    select_num = int(input('어떤 게임을 하시겠습니까? <1번. 배스킨라빈스31 / 2번. 3.6.9>: '))  # 게임 종류 선택
    
    # <1번. 배스킨라빈스31 게임>
    if select_num == 1:             
        people_num = int(input('몇 명이서 진행하시겠습니까?: '))
        print('배스킨~라빈스~31!')   # 인트로 출력
        
        game1_order = 1             # 사람의 순서
        game1_num = 0               # 게임의 현재 숫자
        while True:
            n = random.randint(1,3) # 외칠 숫자 1~3개
            
            # <1-1. 본인의 차례일 경우>
            if game1_order == people_num:
                my_num = list(map(int, input('당신의 차례입니다. 연속된 숫자를 최대 3개 말해주세요: ').split())) # 공백으로 구분하여 입력
                # <*본인이 31을 외쳤을 경우>
                if 31 in my_num:   
                    drink_num += 1  # 술을 한잔 마심
                    print(f'게임에서 패배하셨습니다..술을 한 잔 마셔 총 {drink_num}잔째 입니다.')
                    break           # 게임 종료
                # <본인의 차례를 잘 넘어간 경우>
                else:               
                    game1_order = 1 # 사람들의 차례를 초기화
                    game1_num = max(my_num)
                    
            # <1-2. 본인이 아닌 다른 사람의 차례일 경우>
            else: 
                # <숫자를 1개 외칠 경우>              
                if n == 1:          
                    print(game1_num+1)
                    game1_num += 1  # 현재의 숫자에 +1
                # <숫자를 2개 외칠 경우>    
                elif n == 2:        
                    print(game1_num+1, game1_num+2)
                    game1_num += 2  # 현재의 숫자에 +2
                # <숫자를 3개 외칠 경우>   
                else:               
                    print(game1_num+1, game1_num+2, game1_num+3)
                    game1_num += 3  # 현재의 숫자에 +3
                # <*숫자 31이 나올 경우 게임 종료>  
                if game1_num >= 31: 
                    print('누군가가 31을 외쳐, 배스킨라빈스31 게임을 종료합니다.')
                    break
                    
                game1_order += 1    # 다음 차례로 넘겨주기 위해 +1
                    
    # <2번. 3.6.9 게임>                
    elif select_num == 2:
        people_num = int(input('몇 명이서 진행하시겠습니까?: '))
        print("369~369!369~369!")   # 인트로 출력
        
        game2_order = 1             # 사람의 순서
        game2_num = 1               # 게임의 현재 숫자
        while True:
            # <2-1. 3,6,9를 찾기 위한 문자열 생성>
            new_num = str(game2_num)
            num_3, num_6, num_9 = 0, 0, 0  # 3,6,9의 개수를 저장할 변수
             
            if '3' in new_num:      # 3이 들어가 있을 경우
                num_3 = new_num.count('3') # 3의 개수를 세어 넣어줌
                
            if '6' in new_num:    # 6이 들어가 있을 경우
                num_6 = new_num.count('6') # 6의 개수를 세어 넣어줌
                
            if '9' in new_num:    # 9가 들어가 있을 경우
                num_9 = new_num.count('9') # 9의 개수를 세어 넣어줌
                
            # <2-2. 정답 할당>
            if (num_3 + num_6 + num_9) == 0: # 박수를 칠 때가 아닌 경우
                game2_answer = str(game2_num) # 현재 숫자가 정답이 됨
                
            else:                   # 박수를 쳐야할 경우
                game2_answer = ('짝'*(num_3 + num_6 + num_9)) # 3,6,9의 개수만큼 박수를 쳐야함
                
            # <2-3. 정답 판별>
            # <본인의 차례일 경우>
            if game2_order == people_num:
                my_num2 = input('정답을 입력하세요: ')
                # <정답을 맞춘 경우>
                if my_num2 == game2_answer:
                    game2_order = 1 # 사람들의 차례를 초기화
                    game2_num += 1  # 현재 숫자를 +1
                    continue
                # <*틀린 답을 외쳤을 경우>   
                else:              
                    drink_num += 1  # 술을 한잔 마심
                    print(f'게임에서 패배하셨습니다..술을 한 잔 마셔 총 {drink_num}잔째 입니다.')
                    break           # 게임 종료
                
            # <본인이 아닌 다른 사람의 차례일 경우>
            else:                  
                print(game2_answer) # 숫자 or 박수(짝) 출력
                game2_order += 1 # 다음 차례로 넘겨주기 위해 +1
                game2_num += 1  # 현재 숫자를 +1
                
            # <*숫자가 40이 된 경우>
            if game2_num == 40:
                print('이 게임 누가 하자 했어..다시 하자!')
     
    # <*상태 확인>               
    if drink_num == 3:  # 술을 3잔 마셨을 경우
        print('술을 3잔 마셔 한상호씨가 취해버렸습니다..게임에서 빠집니다..')
        break           