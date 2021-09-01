# 두개의 배열에서 뽑은 두개의 수를 곱해 누적으로 더해서 만들어진 최소의 수를 return 하라


def solution(a, b):
    answer = 0

    arr1 = sorted(a)
    arr2 = sorted(b, reverse=True)

    for i in range(len(arr1)):
        answer += (arr1[i] * arr2[i])

    return answer


print(solution([1, 4, 2], [5, 4, 4]))

# 채점 결과
# 정확성: 69.6
# 효율성: 30.4
# 합계: 100.0 / 100.0
