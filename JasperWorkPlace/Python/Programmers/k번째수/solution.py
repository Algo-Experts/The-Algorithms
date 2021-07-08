#  문제 풀이 순서

#  1. commands 로 들어온 배열 내부의 0번째 배열의 첫번째 원소와 두번째 원소를 이용해서 slice 한후에 정렬하여 새로운 배열(new_array)에 넣는다.
#  2. 1번째의 결과를 이용하여 나온 new_array 의 , commands 배열 내부의 배열의 세번째 원소 번째 값을 answer 배열에 append


def solution(array, commands):
    answer = []

    for i in commands:
        #  1번째 문제 풀이
        new_array = sorted(array[i[0]-1: i[1]])
        #  2번째 문제 풀이
        answer.append(new_array[i[2]-1])

    return answer


# ex_array = [1, 2, 3]
# print(ex_array[0:2])
# 결과값 : [1,2] -> 0 번째 포함 2번째 미만

# sorted( 배열 ) //  (배열).sort // -> 잘 구분하여 사용할것
