

def conv(number, what_digit):
    temp = "0123456789ABCDEF"
    i, j = divmod(number, what_digit)

    if i == 0:
        return temp[j]
    else:
        return conv(i, what_digit) + temp[j]

# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.


def solution(n, t, m, p):
    digits = []
    number = 0
    while (len(digits) < t * m):
        digits += list(conv(number, n))
        number += 1

    answer = ''

    for i in range(t):
        # 본인의 숫자만 가지고 오기
        answer += digits[i * m + (p - 1)]

    return answer


print(conv(7, 2))
print(divmod(1, 2))

print(solution(2, 4, 2, 1))
