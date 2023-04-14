a = str(input("문자를 입력하세요 : "))

if a.lower() == a[::-1].lower():
    print(a,"is a Palindrome!")
else:
    print(a,"is not a Palindrome..")
