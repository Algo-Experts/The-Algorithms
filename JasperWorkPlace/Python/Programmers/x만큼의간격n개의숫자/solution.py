def solution(x, n):
    answer = []
    a = x
    for i in range(n):
        x = a * (i + 1)
        answer.append(x)

    return answer
