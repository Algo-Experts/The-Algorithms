# 문제 설명
# 알파벳 문자열 s 를 n 번씩 밀어서 만들어진 암호를 return
# ex)  s = "AB"  n = 1 return "BC" ,, n = 3 return "DE"
#       s = "z " n = 1 return "a " 소문자 대문자 공백 구분

# 풀이 순서
# 1. 각각의 알파벳 대문자와 소문자 리스트를 만들어 주기 위해 string 모듈 import
# 2. s 의 알파벳을 돌면서 대문자인지 소문자인지를 체크한다
# 3. 알파벳은 26자이므로 z 에서 이동하는 숫자가 있을 경우 다시 a 로 이동 해야 하기 때문에 26을 나눈 나머지로 위치 이동
# 4. answer 에 나온 숫자들을 더해주는데, 공백이 들어왔을 경우에는 그대로 공백을 보내줌

import string


def solution(s, n):
    answer = ""

    lowerAlphabetList = list(string.ascii_lowercase)
    upperAlphabetList = list(string.ascii_uppercase)

    for alphabet in s:
        if alphabet in lowerAlphabetList:

            positionAlphabet = lowerAlphabetList.index(alphabet) + n

            answer += lowerAlphabetList[positionAlphabet % 26]

        elif alphabet in upperAlphabetList:

            positionAlphabet = upperAlphabetList.index(alphabet) + n

            answer += upperAlphabetList[positionAlphabet % 26]

        else:

            answer += " "

    return answer


print(solution("z Z", 2))
