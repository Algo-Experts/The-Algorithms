

def solution(land):
    answer = 0
    max_num_index = 0
    count = 0

    for column in range(len(land) + 1):
        count += 1

        first_step = max(land[column])
        print("더해지는 수 ", first_step)

        answer += first_step

        max_num_index = land[column].index(first_step)

        if (count == len(land)):
            return answer
        else:
            land[column+1][max_num_index] = 0

        print(count)


# print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))

# print(solution([[1, 2, 3, 4], [5, 6, 7, 8],
#                 [9, 10, 11, 12], [13, 14, 15, 16], [8, 9, 1, 3], [8, 9, 1, 100]]))

a = [1, 2, 3]


def final_solution(land):

    for column in range(1, len(land)):
        for column_num in range(4):
            land[column][column_num] += max(land[column-1]
                                            [0:column_num] + land[column - 1][column_num+1:])

    return max(land[-1])


print(final_solution([[1, 2, 3, 4], [5, 6, 7, 8],
                      [9, 10, 11, 12], [13, 14, 15, 16], [8, 9, 1, 3], [8, 9, 1, 100]]))

# 정확성: 59.8
# 효율성: 40.2
# 합계: 100.0 / 100.0
