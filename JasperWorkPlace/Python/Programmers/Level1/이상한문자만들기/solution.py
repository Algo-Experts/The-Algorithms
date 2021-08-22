def solution(s):

    a = list(s.split(" "))
    b = []
    for word in a:
        change = []
        for alpha in range(len(word)):
            if alpha % 2 == 0:
                change.append(word[alpha].upper())
            else:
                change.append(word[alpha].lower())
        b.append("".join(change))

    return " ".join(b)


# print(solution("try hello world"))
