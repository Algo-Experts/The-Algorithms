# 살짝 긴 문제

# 4번 학생은 3번 학생에게, 5번 학생에게만 옷을 빌려 줄수 있다.

# 전체 학생의 수가 n / 체육복을 도난 당한 삭생들의 번호의 배열 lost / 여벌의 체육복을 가져온 학생들의 배열 reserve

#  체육수업을 들을수 있는 학생의 최댓값을 return

# ex) n = 5 / lost = {2,4} / reserve = {1,3,5} / return = 5

#  전체 학생수는 2~30 / 도난 당한 학생수와 여벌 체육복 학생수는 1명이상 / 여벌 옷을 가져온 학생이 도난 당했을 수 있음 이때는 다른 학생에게 못빌려줌

#  문제 풀이 순서
#  1. 도난 당한 학생과 여분의 옷이 있는 학생이 겹치는 것을 제거한다. (lost 배열과 reserve 배열의 중복 제거 두개의 배열 모두 제거해서 해당 배열에 넣어준다.)
#  중복 제거한 도난 번호 배열 -> lost_new / 중복 제거한 여분 여분 옷 번호 배열 -> reserve_new

#  2. 여분 옷 있는 배열의 -1 번호 , +1 번호를 체크

#  3. 2 번의 번호들이 lost_new 에 있다면 lost_new 배열에서 제거 ! -> 완전히 수업에 참여 못하는 학생들

#  4. 위에서 나온 배열의 길이를 총 학생수에서 뺌 return

def solution(n, lost, reserve):

    # 1번 풀이 순서
    lost_new = [a for a in lost if a not in reserve]
    reserve_new = [b for b in reserve if b not in lost]

    for i in reserve_new:
        # 2번 풀이 순서
        left_student = i - 1
        right_student = i + 1

        # 3번 풀이 순서
        if left_student in lost_new:
            lost_new.remove(left_student)
        elif right_student in lost_new:
            lost_new.remove(right_student)

    return n - len(lost_new)
