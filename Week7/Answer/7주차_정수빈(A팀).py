num_list=['0001','0004','0025','0052','0054','0080','0083','0132','0393']
name_list=['이상해씨','파이리','꼬부기','피카츄','냐옹','고라파덕','야도란','파오리','메타몽','팽도리']
poket_dict={}
i=0


for n in num_list:
    poket_dict[n]=name_list[i]
    i+=1

while True:
    num=input('{} 앞 번호들 중 포켓몬 이름을 알고 싶은 번호를 입력해주세요: '.format(num_list))
    if num in num_list:
        name=poket_dict[num]
        print('No.{}은 {}입니다!'.format(num,name))
    else :
        print("현재 도감에 없는 번호입니다:(")

    con=input('더 알아보시겠습니까?(Y/N): ')
    
    # 멘토: con.lower() == 'y'로 해주셔야 맞게 작동됩니다! 나머지는 다 잘해주셨어요 :)
    if con.lower==y:
        continue
    else:
        print("포켓몬 도감을 종료합니다: ")
        break
    
