def solution(arr1, arr2):
    answer = []

    for inner in range(len(arr1)):
        tempArray = []
        for minner in range(len(arr1[inner])):
            tempArray.append(
                arr1[inner][minner] + arr2[inner][minner])

        answer.append(tempArray)

    return answer


# arr1 = [[1], [2]]

# arr2 = [[3], [6]]

# print(solution(arr1, arr2))
