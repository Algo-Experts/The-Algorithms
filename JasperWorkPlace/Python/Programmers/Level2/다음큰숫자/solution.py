# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다

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
