num_lst = ['0001', '0004', '0007', '0025', '0052', '0054', '0080', '0083', '0132', '0393']
name_lst = ['이상해씨', '파이리', '꼬부기', '피카츄', '나옹', '고라파덕', '야도란', '파오리', '메타몽', '팽도리']
poket_dict = {}
for i in range(len(num_lst)):
    poket_dict[num_lst[i]] = name_lst[i]
while 1:
    x = int(input('앞 번호들 중 포켓몬 이름을 알고 싶은 번호를 입력해주세요 : '))
    x1 = '{0:04d}'.format(x) 
    if x1 in num_lst:
        print('No.{}은(는) {}입니다!'.format(x,poket_dict.get(x1)))
    else:
        print('현재 도감에 없는 번호입니다:(')

    # 멘토: 다 너무 잘해주셨는데, 여기서 input 안에 print를 넣어서 None까지 같이 출력되고 있어요. print는 빼주시면 됩니다!
    response = input('더 알아보시겠습니까?(Y/N):')
    if response.upper() == 'N':
        print('포켓몬 도감을 종료합니다 :)')
        break
    else:
        continue
    
        
