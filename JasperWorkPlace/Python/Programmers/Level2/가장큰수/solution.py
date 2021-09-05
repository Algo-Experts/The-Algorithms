# 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.


def solution(numbers):
    res = []

    for number in numbers:
        prev = str(number)
        add = list(str(number))

        i = 0
        while len(add) < 4:
            add.append(prev[i])
            i = (i + 1) % len(prev)
        add = int("".join(add))
        res.append([add, prev])

    res = sorted(res, reverse=True)
    return str(int("".join(unit[1] for unit in res)))


print(solution([6, 10, 2]))


# print("".join(some))
