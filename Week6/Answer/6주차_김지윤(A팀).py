total = 0

for n in range(1,201):
    if n%7 == 0:
        if n%28 == 0:
            print("{}은 7의 배수지만 4의 배수라서 싫어 :(".format(n))
        else:
            print("{}은 내가 좋아하는 7의 배수니까 더해야지 :)".format(n))
            total += n
print("좋아하는 숫자만 더한 값 : {}".format(total))
