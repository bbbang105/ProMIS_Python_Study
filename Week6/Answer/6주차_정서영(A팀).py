total = 0
for num in range(1,201):
    if num % 7 == 0:
        if num % 4 == 0:
            print('상욱: {}는 7의 배수지만 4의 배수라서 싫어:('.format(num))
        else:
            total += num
            print('상욱: {}은 내가 좋아하는 7의 배수니까 더해야지 :)'.format(num))
print('좋아하는 숫자만 더한 값:{}'.format(total))
