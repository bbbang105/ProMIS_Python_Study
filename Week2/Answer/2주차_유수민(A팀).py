palindrome = input("문자를 입력하세요.")
palindrome = palindrome.replace(" ","")
palindrome = palindrome.lower()
palindrome_reverse=''

for i in palindrome:
    palindrome_reverse = i + palindrome_reverse

print("뒤집은 문자는:", palindrome_reverse)

if palindrome == palindrome_reverse:
    print("입력값 is a Palindrome!")
else:
    print("입력값 is not a Palindrome..")
