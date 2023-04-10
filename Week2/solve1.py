word = input()          # 입력값 받기
re_word = word[::-1]    # 문자열 뒤집기

if word.lower() == re_word.lower(): # 맞을 시
    print(word + ' is a Palindrome!')
else:                               # 틀릴 시
    print(word + ' is not a Palindrome..')

