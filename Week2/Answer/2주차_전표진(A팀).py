a = input("입력하세요.")
a = a.lower()

if a==a[::-1]:
    print("입력값 is a Palindrome!")
else:
    print("입력값 is nat a Palindrome..")
