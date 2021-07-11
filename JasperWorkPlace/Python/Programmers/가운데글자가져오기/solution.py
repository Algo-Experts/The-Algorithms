# 일요일이니 간단한 문제로 시작 !

# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 풀이 순서
#  1. String s 를 list 형태로 변환 한뒤
#  2. 길이가 짝수인지 홀수 인지 판단하여
#  3. 짝수이면 가운데 것 2개를 뽑고
#  4. 홀수이면 가운데 하나를 뽑는다.


def solution(s):
    answer = ''
    a = list(s)

    if len(a) % 2 == 0:
        b = len(a) // 2
        answer = a[b-1] + a[b]
    else:
        b = len(a) // 2
        answer = a[b]

    return answer


print(solution("qwer"))
