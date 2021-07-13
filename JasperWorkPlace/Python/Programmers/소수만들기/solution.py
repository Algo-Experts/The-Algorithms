# 문제 설명
# nums 가 배열로 들어올때, ( 중복 x )
# nums 에 있는 숫자 서로 다른 숫자 3개를 골라
# 소수가 되는 경우의 수를 return
# 풀이 순서
# 1. nums 에 있는 수를 차례로 3개씩 뽑아 더해준다. -> combinations 함수 사용
# 2. 더해준 값이 소수가 아닐때 n 을 넣어주는 check_list 선언
# 3. 만약 더해준 값이 1이면 바로 answer = 0 던져줌
# 4. 소수 판별  : 자기 자신 전까지 나눠 주며 나머지가 0이 나오면
#   소수 아님 check_list "n" 값 넣어줌 그리고 break 로 반복문 탈출
# 5. total nums 의 수를 total 에 넣었으므로 total - check_list의 크기 만큼 해주면 됨


from itertools import combinations


def solution(nums):
    answer = -1
    check_list = []
    total = len(list(combinations(nums, 3)))
    for num in combinations(nums, 3):

        if sum(num) == 1:
            check_list.append("n")
            answer = 0
            return

        else:
            for i in range(2, sum(num)):
                if(sum(num) % i == 0):
                    check_list.append("n")
                    break

        answer = total - len(check_list)

    return answer


# print(solution([1, 2, 7, 6, 4]))
