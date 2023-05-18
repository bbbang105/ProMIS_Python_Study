result = 0
for num in range(7,201,7):
    if num % 4 == 0:
        print(f'상욱: {num}은 7의 배수지만 4의 배수라서 싫어 :(')
        continue
    print(f'상욱: {num}은 내가 좋아하는 7의 배수니까 더해야지 :)')
    result += num
    
print(f'좋아하는 숫자만 더한 값: {result}')

# num = 7
# result = 0
# while num <= 200:
#     if num % 4 == 0:
#         print(f'상욱: {num}은 7의 배수지만 4의 배수라서 싫어 :(')
#     else:
#         print(f'상욱: {num}은 내가 좋아하는 7의 배수니까 더해야지 :)')
#         result += num
#     num += 7
    
# print(f'좋아하는 숫자만 더한 값: {result}')
