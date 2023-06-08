score_lst = [76, 53, 63, 55, 23, 97, 99, 23, 100, 65, 77, 55, 99, 53, 15, 9, 6, 2]

while True:
    score = int(input('학생의 점수를 입력해주세요: '))
    
    if score < 0 or score > 100: # 올바르지 않은 점수 입력일 경우
        print('범위를 초과했습니다. 점수를 다시 입력해주세요!')
        continue
    
    score_lst.append(score)  # list에 추가
    score_lst = sorted(score_lst, reverse = True)  # 등수를 알기 위해 내림차순으로 정렬
    grade = (score_lst.index(score) + 1)  # 등수 계산
    same = score_lst.count(score) - 1  # 동점자의 수
    average = sum(score_lst) / len(score_lst)  # 평균 계산
    average = round(average)  # 소숫점 반올림
      
    print(f'현재 학생의 등수는 {grade}등이며, 동점자가 {same}명 존재합니다.')
    print(f'학생들의 평균은 {average}점 입니다.')
    
    temp = input('계속 하시겠습니까?(Y/N): ')
    if temp == 'N':
        print('시스템을 종료합니다.')
        break