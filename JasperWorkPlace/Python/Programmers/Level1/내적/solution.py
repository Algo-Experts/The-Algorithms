# 짧은 문제

# 풀이 과정
#  1. 각 배열에서 원소를 빼와 answer 에 더해준다.
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i] * b[i])
    return answer


print(solution(a, b))
