def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
    while b - a != 1 or a % 2 == 0:
        answer += 1
        if a % 2 == 1:
            a = (a + 1) / 2
        else:
            a = a / 2
        if b % 2 == 1:
            b = (b + 1) / 2
        else:
            b = b / 2
    answer += 1
    return answer
