seven = 0

# 멘토: 시작을 1로 설정해서 숫자가 1,8,15..이렇게 들어가고 있어요. 
# 그래서 시작을 7로 바꿔서 range(7,201,7)로 해주시면 출력이 옳게 나옵니다!
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

    
