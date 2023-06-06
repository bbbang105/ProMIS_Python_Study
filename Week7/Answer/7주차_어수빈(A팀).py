num_lst = ['0001', '0004', '0007', '0025', '0052', '0054', '0080', '0083', '0132', '0393']
name_lst = ['이상해씨', '파이리', '꼬부기', '피카츄', '나옹', '고라파덕', '야도란', '파오리', '메타몽', '팽도리']
poket_dict = dict(zip(num_lst, name_lst))

while True:
    print(num_lst)
    ent_num = input()

    if ent_num not in num_lst:
        print('현재 도감에 없는 번호입니다:(')
    else:
        name = poket_dict[ent_num]
        print('No.<{}>은(는) <{}>입니다!'.format(ent_num, name))

    keep = input('더 알아보시겠습니까?(Y/N):')
    if keep.lower() == 'y':
        continue
    else:
        print('포켓몬 도감을 종료합니다 :)')
        break
 

