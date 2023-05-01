import random
#모르겠어요...
while True:
    x = random.randrange(1.13)                  # 멘토: random.randint(1,12)로 써주시면 됩니다!
    print('Q : '+x+'월은 며칠까지 있을까요?')     # 숫자랑 문자열은 +가 안돼서, 포멧팅이나 ','로 합쳐주셔야 해요.
    answer = int(input(print('')))              # answer = int(input('A. '))로 수정하면
    print('A :', answer)                        # 이 코드는 빼주셔도 됩니다!
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12 : # 하나하나 다 적으면 오래걸리니까 리스트로 묶어주면 좋아요.
        if answer == 31:
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 31일입니다.')
    elif x == 4 or x == 6 or x == 9 or x == 11:
        if answer == 30:
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 30일입니다.')
    else:
        if answer == 28:
            print('정답입니다!')
        else:
            print('틀렸습니다..정답은 30일입니다.') # 30일 => 28일
            
    back = input('다시하시겠습니?(Y/N)')
    if back.lower() == 'y':
        print('게임을 다시 시작하겠습니다.','\n')
    else:
        print('게임을 종료합니다:)')
        break
    


