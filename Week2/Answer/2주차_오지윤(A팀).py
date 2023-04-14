#입출력문

word = str(input("Enter word:"))

#문자열 거꾸로 뒤집기
#if 문 사용

if word.lower() == word[::-1].lower():
    print(word,'is a Palindrome!')

else:
    print(word, 'is not a Palindrome..')
