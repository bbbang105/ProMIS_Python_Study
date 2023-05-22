seven = 0

for i in range(1,201,7):
    if i%7 == 0:
        if i%4 == 0:
            print("상욱: %d은 7의 배수지만 4의 배수라서 싫어:(" %i)
        else:
            seven += i
            print("상욱: %d은 내가 좋아하는 7의 배수니까 더해야지 :)" %i)
    else:
        continue

print("좋아하는 숫자만 더한 값: %d" %seven)

    
