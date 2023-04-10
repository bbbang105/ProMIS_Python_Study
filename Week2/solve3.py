word = input()          # 입력값 받기
word_lst = list(word)   # 문자열을 리스트로 변환
word_lst.reverse()      # 리스트 뒤집기
re_word = ''.join(word_lst) # join 메소드를 사용하여 다시 문자열로 변환

if word.lower() == re_word.lower(): # 맞을 시
    print(word + ' is a Palindrome!')
else:                               # 틀릴 시
    print(word + ' is not a Palindrome..')
