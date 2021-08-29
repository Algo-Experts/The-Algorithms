# 문자열 자르는 것이기 때문에, 이진 탐색의 개념이 많이 들어간듯 하다.
# 처음에는 하나씩 쪼개고, 그 다음에는 두개씩, 세개씩 쪼개는 형식으로 for 문을 돌린다.
# 그 중 길이가 제일 작은 값은 return 한다.


def solution(s):
    result = []
    # 만약. 문자열의 길이가 1이라고 하면, 간단하게 1을 반환 해주고
    if len(s) == 1:
        return 1
    # 문자열을 반으로 나누어 ( 가장 큰 단위 부터 나누어 )
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j+1]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        result.append(len(b))

    return min(result)


# k = "aabbccdd"

# print(k[:1])

# for i in range(1, len(k)//2 + 1):
#     print(k[i])
