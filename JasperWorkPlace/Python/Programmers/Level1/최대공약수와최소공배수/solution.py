# 문제 설명 : n 과 m 의 최소공배수와 최대 공약수를 구하여라.

# 문제 풀이 : n 과 m 의 곱이 결국에는 최소 공배수와 최대 공약수의 곱이라는 것을 알고 풀면 된다.

def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)

    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1


def solution(n, m):
    return [gcd(n, m), (n * m) / gcd(n, m)]
