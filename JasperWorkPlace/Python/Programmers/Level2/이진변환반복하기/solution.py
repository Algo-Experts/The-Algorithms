def solution(s):
    a, b = 0, 0 	# 이진 변환의 횟수, 제거된 모든 0의 개수
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num		# s의 길이-1의 개수=0의 개수
        s = bin(num)[2:]		# 이진 변환
    return [a, b]


# print(solution("110010101001"))
