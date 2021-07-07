# 문제 풀이 순서
# 1. numbers 배열 안에서 각각의 원소를 더한다.
# 2. 중복되는 것 없애주고, 정렬해준다.

def solution(numbers):
    unSorted_answer = []

# 1번째 단계 - 전체 범위의 배열 에서
    for i in range(0, len(numbers) - 1):
        # 1번째 단계 - 앞에 있는 수들 모두 더한후
        for j in numbers[i + 1:]:
            # 1번째 단계 - 배열에 넣어준다.
            unSorted_answer.append(numbers[i] + j)
        # 2번째 단계 중복 을 없애 주기 위해 집합 메서드 set 과 정렬을 위해 sorted(list()) 사용
    return sorted(list(set(unSorted_answer)))


#  array slice 시에 for 문 안에서 저렇게 0번째 부터 2 번째 까지 뽑을 수 있다.
# array_example = [1, 2, 3, 4]

# for i in array_example[0:3]:
#     print(array_example[i-1])
