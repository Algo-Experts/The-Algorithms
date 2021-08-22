def solution(s):
    answer = True

    p = 0
    y = 0

    new_s = s.lower()

    for alpha in new_s:
        if alpha == "p":
            p += 1
        elif alpha == "y":
            y += 1
    if p != y:
        answer = False

    return answer


# true
print(solution("pPoooyY"))

# false
print(solution("Pyy"))
