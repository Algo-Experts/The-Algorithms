def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


def solution(arr):
    answer = 0
    arr.sort(reverse=True)

    for i in range(len(arr)-1):
        b = gcd(arr[i], arr[i+1])

        arr[i+1] = (arr[i]*arr[i+1]) / b

    answer = arr[-1]
    return answer
