# JadenCase란 모든 단어의 첫 문자가 대문자이고,
# 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때,
#  s를 JadenCase로 바꾼 문자열을 리턴하는 함수,
#  solution을 완성해주세요.


def solution(s):
    answer = ''
    for idx, i in enumerate(s):
        if (idx == 0):
            answer = i.upper()
        elif s[idx-1] == ' ':
            answer = ''.join([answer, i.upper()])
        else:
            answer = ''.join([answer, i.lower()])
    return answer


# print(solution("3people unFollowed me"))


something = "people unFollowed me"


answer = ''

for a, b in enumerate(something):
    if a == 0:
        answer += b.upper()

    elif something[a-1] == ' ':

        answer += (b.upper())

    else:
        answer += b.lower()

print(answer)
