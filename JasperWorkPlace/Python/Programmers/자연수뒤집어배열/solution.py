# 문제 설명
# 자연수 n 이 입력됨
# 숫자를 원소로 가지는 배열 형태로 리턴

# 문제 풀이 순서
# 1. 숫자를 문자열로 변환하여 뒤집은 다음 그걸 리스트로 만듬
# 2. 1번 순서에서 만들어진 배열의 원소들을 int 로 형변환


def solution(n):
    answer = []

#   순서 1
    nums = list(reversed(list(str(n))))

#   순서 2
    for num in nums:
        answer.append(int(num))

    return answer
