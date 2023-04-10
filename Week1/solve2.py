sen = 'i lovee promis'

x = 'ilpms' # 바꿀 문자를 지정
y = 'ILPMS' # x에서 지정한 문자를 대체할 문자

trans = sen.maketrans(x,y) # 문자열 대체 매핑 테이블 설정
new_sen = sen.translate(trans) # 대체하여 새로운 문장 생성

print('유다현: ' + new_sen[:6] + new_sen[7:] + '!') # 문자열 슬라이싱, 이어붙이기