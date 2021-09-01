def solution(n):
    one_count = format(n, 'b').count("1")

    while(True):
        n += 1
        if one_count == format(n, 'b').count("1"):
            return n


print(solution(15))

# 채점 결과
# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0
