num_lst = ['0001', '0004', '0007', '0025', '0052', '0054', '0080', '0083', '0132','0393']
name_lst = ['이상해씨', '파이리', '꼬부기', '피카츄', '나옹', '고라파덕', '야도란', '파오리', '메타몽', '팽도리']
poket_dict = {}
for i in range(10): # 인덱스를 통해 접근
    poket_dict[num_lst[i]] = name_lst[i] # 딕셔너리에 넣어줌
print(poket_dict)

while True:    
    num = input(f'{num_lst} 앞 번호들 중 포켓몬 이름을 알고 싶은 번호를 입력해주세요: ') # num_lst 함께 출력
    if num not in poket_dict: # 사전에 없는 번호일 경우
        print('현재 도감에 없는 번호입니다:(')
        continue
    
    name = poket_dict[num] # 입력된 번호에 해당하는 포켓몬 이름
    print(f'No.{num}은(는) {name}입니다!' )
    
    temp = input('더 알아보시겠습니까?(Y/N): ')
    if temp == 'N':
        print('포켓몬 도감을 종료합니다 :)')
        break