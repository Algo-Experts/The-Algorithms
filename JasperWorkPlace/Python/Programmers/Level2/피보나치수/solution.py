# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2)
# 2 이상의 n이 입력되었을 때, n 번째 피보나치 수를 1234567 으로 나눈 나머지를 리턴하는 함수 나타내기

# fibo 를 구해보자


def get_fibo(n):

    fibo_array = [0, 1]
    for _ in range(n):
        fibo_array.append(fibo_array[-1] + fibo_array[-2])

    return fibo_array[n]


def solution(n):
    answer = (get_fibo(n) % 1234567)
    return answer


print(solution(5))
