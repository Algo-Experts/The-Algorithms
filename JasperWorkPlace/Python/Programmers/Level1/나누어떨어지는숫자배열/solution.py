def solution(arr, divisor):
    answer = []

    for num in arr:
        if(num % divisor == 0):
            answer.append(num)

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()

    return answer


print(solution([2, 36, 1, 3], 1))

print(solution([1, 2, 3], 5))
