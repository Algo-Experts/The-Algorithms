
# 문제 풀이 순서
#
# 배열의 길이가 1일때는 [-1] 을 return 해주고,
# 아닐때는 가장 작은 배열의 원소를 제거하고, return 해줘야 한다.
#
# 1. 해당하는 if 문 내부에,
#
# min(array) -> 배열에서 가장 작은 '숫자'를 리턴
# 배열.index(원소) 을 이용해서 배열의 몇번째 값인지 확인
# 배열,pop 을 통해서 배열 내부의 값을 뿅 없앤다 .


def solution(arr):

    if len(arr) > 1:
        print(min(arr))
        arr.pop(arr.index(min(arr)))
    else:
        arr = [-1]

    return arr


# print(solution([2, 1, 3, 4]))
