count=0
for n in range(7, 201):
    if n%7==0 and n%4==0:
        print(n,"은 7의 배수이지만 4의 배수라서 싫어 :(")

    elif n%7==0 and n%4!=0:
        print(n,"은 내가 좋아하는 7의 배수니까 더해야지 :)")
        count+=1
    n+=1
print("좋아하는 숫자만 더한 값", count)
