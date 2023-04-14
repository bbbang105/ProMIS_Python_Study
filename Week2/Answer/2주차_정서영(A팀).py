a = input("입력값: ")


if a.upper() == a[::-1].upper():
    print(a, "is a Palindrome!")

else:
    print(a, "is not a Palindrome..")
