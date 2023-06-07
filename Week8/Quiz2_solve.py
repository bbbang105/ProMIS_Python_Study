A_time = ['소영', '영현', '선우', '상호', '표진', '서영', '후동', '지윤', '수빈', '다현']
B_time = ['수민', '다현', '민정', '지인', '현지', '상욱', '혜은', '형석', '상호', '효환']

# 집합으로 변환
A_time = set(A_time)
B_time = set(B_time)

# 교집합으로 범인 찾기
criminal = A_time.intersection(B_time)
# criminal = A_time & B_time

# 합집합으로 총 먹은 사람 수 구하기
eat_num = A_time.union(B_time)
# eat_num = A_time | B_time

print(f'햄버거를 2개나 먹은 사람은 {criminal} 입니다!')
print(f'햄버거를 먹은 인원은 {len(eat_num)}명 입니다!')