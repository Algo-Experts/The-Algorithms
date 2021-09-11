from itertools import permutations


def solution(numbers):
    answer = 0

    num_array = [i for i in numbers]
    combination_array = []

    for i in range(1, len(num_array) + 1):
        nums = permutations(num_array, i)
        for num in nums:
            get_combination = int("".join(num))
            combination_array.append(get_combination)

    print(combination_array)
    for n in set(combination_array):
        count = 0
        for j in range(2, n):
            if n % j == 0:
                count += 1
                break
        if n > 1 and count == 0:
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))
