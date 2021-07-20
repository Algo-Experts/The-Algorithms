# 문제 설명
# 반복되는 수 제외
# [1,1,3,3,0,1,1] 이 들어올 경우 [1,3,0,1] 로 리턴

#  문제 풀이
#  1. 마지막 배열인덱싱 해서 배열의 형태로 마지막 숫자만 보여주면서 같으면 continue  틀리면 배열에 넣어줌


def solution(arr):
    answer = []

    for num in arr:

        if answer[-1:] == [num]:

            continue
        else:
            answer.append(num)

    return answer
