a=0
for i in range(201):
    if i%7==0:
        if i%28==0:
            continue
        a+=i
        print("상욱:",i, "은 내가 좋아하는 7의 배수니까 더해야지 :)")
    print("좋아하는 숫자만 더한 값:", a)
        
        
