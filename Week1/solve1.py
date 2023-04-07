sen = 'i lovee promis'

new_sen = sen[:5] + sen[6:-3] # 문자열 슬라이싱을 통해 e와 mis 제거
up_mis = sen[-3:].upper() # upper() 메소드를 사용해 대문자 MIS 생성

print(new_sen.title() + up_mis + '!') # title() 메소드를 사용, 문자열 이어 붙여 출력