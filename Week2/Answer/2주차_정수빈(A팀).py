a=input("사용자로부터 입력값을 받습니다: ")
if a.lower()==a[::-1].lower():
    print(a,"is a Palindrome!")
else :
    print(a,"is not a Palindrome..")
