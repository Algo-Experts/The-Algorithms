# 각각의 최소공배수를 구해서 나타내면 되는 것으로 보인다.
# For example, if the array is [ 2 , 6,8, 14] 이면, 2 와 6의 최소공배수 를 a 로 가정하면,  a 와 8의 최
# 소 공배수를 다시 b 로 그리고 b 와 14 의 최소공배수가 바로 정답이 나온다.,


# 최대공약수 뽑는 알고
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a


def solution(arr):
    answer = 0
    arr.sort(reverse=True)

    for i in range(len(arr)-1):
        b = gcd(arr[i], arr[i+1])

        arr[i+1] = (arr[i]*arr[i+1]) / b

    answer = arr[-1]
    return answer


print(gcd(3, 4))
