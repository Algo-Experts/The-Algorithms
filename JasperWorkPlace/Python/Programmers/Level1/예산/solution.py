# 문제 설명
# d -> [부서 1에서 : 1, 부서 2에서 : 3,부서 3에서 : 2, 부서 4에서 : 5, 부서 5에서 : 4] //  budget ->  9 일경우

# 문제 풀이 순서

# 1. 사용 되어진 돈을 저장 하는 변수 used_money 를 생성 해준다.
# 2. 적은 돈 부터 사용되어지게끔 sorted 함수 사용 하여 정렬 해준다.
# 3. budget 보다 used_money 가 적을때 까지 진행 한다.
# 4. 진행 될때 마다 answer 에 1을 더해준다.


def solution(d, budget):
    answer = 0

    # 1 단계
    used_money = 0

    # 2 단계
    new_d = sorted(d)

    #
    for need_money in new_d:
        used_money += need_money
        # 3 단계
        if budget < used_money:
            break
        # 4 단계
        answer += 1
    return answer
