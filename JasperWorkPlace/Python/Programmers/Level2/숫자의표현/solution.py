# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

def solution(n):
    answer_count = 0

    for i in range(1, n+1):
        sum_n = 0
        for j in range(i, n + 1):
            sum_n += j
            if (sum_n == n):
                answer_count += 1
                break
            elif sum_n > n:
                break
    return answer_count


# print(solution(3))
# 채점 결과
# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0
