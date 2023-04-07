sen = 'i lovee promis'

org = 'ilpms' 
sub = 'ILPMS' # 변환할 문자들 지정

for i in range(5): # 5번 반복
    sen = sen.replace(org[i], sub[i]) # replace() 메소드를 사용하여 문자 대체

print(sen[:6] + sen[7:] + '!')