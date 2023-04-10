word = input()          # 입력값 받기
re_word = ''            # 뒤집을 문자열 생성

for x in word:
    re_word = x + re_word # 앞에다가 하나씩 문자를 추가
    
if word.lower() == re_word.lower(): # 맞을 시
    print(word + ' is a Palindrome!')
else:                               # 틀릴 시
    print(word + ' is not a Palindrome..')