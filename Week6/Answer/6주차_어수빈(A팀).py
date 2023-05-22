total = 0
for i in range(0,201,7):
        if i==0:
            continue
        elif i%4==0:
            print('상욱: {}은 7의 배수지만 4의 배수라서 싫어 :('.format(i))
        else:
            total+=i
            print('상욱: {}은 내가 좋아하는 7의 배수니까 더해야지 :)'.format(i))

print('좋아하는 숫자만 더한 값:', total)
