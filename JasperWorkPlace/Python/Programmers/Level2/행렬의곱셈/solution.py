# 일단 행렬이 나왔을때는 numpy 사용하는 것을 염두해 두고 있는데,
# numpy 를 쓰지 않고 계산하는 방법으로 먼저 구현을 한다음에,
# numpy 를 사용하고 구현해봐야지!

import numpy as np

# @@@@넘파이 안쓰고 도전


def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        answer_array = []
        for j in range(len(arr2[0])):
            answer_num = 0
            for k in range(len(arr1[0])):
                a = arr1[i][k]
                b = arr2[k][j]
                answer_num += a * b
            answer_array.append(answer_num)
        answer.append(answer_array)

    return answer


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
               [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

# arr1 = [[1, 4], [3, 2], [4, 1]]

# print(arr1[0][1])

# @@@@넘파이 쓰고 도전


def numpy_solution(arr1, arr2):

    answer = (np.matrix(arr1) * np.matrix(arr2)).tolist()

    return answer


print(numpy_solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
                     [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
