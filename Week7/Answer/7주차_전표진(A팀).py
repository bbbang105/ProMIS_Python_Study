num_lst = ['0001', '0004', '0007', '0025', '0052', '0054', '0080', '0083', '0132','0393']
name_lst = ['이상해씨', '파이리', '꼬부기', '피카츄', '나옹', '고라파덕', '야도란', '파오리', '메타몽', '팽도리']
poket_dict = {}

for num in range(len(num_lst)):
    poket_dict[num_lst[num]] = name_lst[num]

while True:
    user = input("{} 앞 번호들 중 포켓몬 이름을 알고 싶은 번호를 입력해주세요.".format(num_lst))
    
    if user not in num_lst:
        print("현재 도감에 없는 번호입니다.")
        continue
    
    else:
        print("No. {}는 {}입니다!".format(user, poket_dict[user]))

    retry = input("더 알아보시겠습니까? (Y/N)")
    if retry[0].lower() == "n":
        print("포켓몬 도감을 종료합니다.")
        break
    
