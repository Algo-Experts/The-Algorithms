
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다.
#  left부터 right까지의 모든 수들 중에서,
#  약수의 개수가 짝수인 수는 더하고,
#  약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

#  플이 순서
#  1. left right 까지의 모든 수를 담는 nums 배열 ,
#     nums 의 원소의 약수를 담는 배열 get_array ,
#     nums 의 원소와 약수를 담는 get_dict 선언
#  2. 용도에 맞게 담은 다음에 약수의 갯수가 짝수이면 answer 에 더하고 홀수면 뺀다.


def solution(left, right):
    answer = 0

#  1번 풀이 순서
    nums = []

    get_array = []

    get_dict = {}

#  2번 풀이 순서
    for i in range(left, right+1):
        nums.append(i)
        for j in range(1, i + 1):
            if i % j == 0:
                get_array.append(j)
                if(i == j):
                    get_dict[i] = get_array
                    get_array = []

    for num in nums:
        if(len(get_dict[num]) % 2 == 0):
            answer += num
        else:
            answer -= num

    return answer


print(solution(13, 17))
