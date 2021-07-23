# 문자열로 구성된 리스트 strings 와,
# 정수 n이 주어졌을때, 각 문자열의 인덱스 n 번째 글자를 기준으로 오름차순 정렬하려 합니다.

# "sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] .

# "abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"]

def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


# strings = ["sun", "bed", "car"]

# n = 2

# print(solution(strings, n))
