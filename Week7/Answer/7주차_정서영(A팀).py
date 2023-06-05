num_lst = ['0001', '0004', '0007', '0025', '0052', '0054', '0080', '0083', '0132', '0393']
name_lst = ['이상해씨', '파이리', '꼬부기', '피카츄', '나옹', '고라파덕', '야도란', '파오리', '메타몽', '팽도리']
poket_dict = {}

for i in range(len(num_lst)):
    poket_dict[num_lst[i]] = name_lst[i]

while True:
    num = input('{} 앞 번호들 중 포켓몬 이름을 알고 싶은 번호를 입력해주세요: '.format(num_lst))

    if num in num_lst:
        name = poket_dict[num]
        print('No.{}은(는) {}입니다!'.format(num,name))
    else:
        print('현재 도감에 없는 번호입니다:(')


    more = input('더 알아보시겠습니까? (Y/N): ')
    if more.lower() == 'n':
        print('포켓몬 도감을 종료합니다:)')
        break
