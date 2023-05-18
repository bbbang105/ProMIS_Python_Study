#for를 이용한 풀이
total = 0
for i in range(1,201):
    if i % 7 == 0:
        if i % 4 == 0:
            print('상욱 : {}은 7의 배수지만 4의 배수니까 싫어 :('.format(i))
        else:
            print('상욱 : {}은 내가 좋아하는 7의 배수니까 더해야지 :)'.format(i))
            total += i
print('좋아하는 숫자만 더한 값 : {}'.format(total))

#while을 이용한 풀이
i = 1
total = 0
while i <= 200:
    if i % 7 == 0:
        if i % 4 == 0:
            print('상욱 : {}은 7의 배수지만 4의 배수니까 싫어 :('.format(i))
        else:
            print('상욱 : {}은 내가 좋아하는 7의 배수니까 더해야지 :)'.format(i))
            total += i
    i+=1        
print('좋아하는 숫자만 더한 값 : {}\n'.format(total))
print('**************************************************\n')