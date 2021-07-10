#  문제 설명 : 2016년 a월 b일 은 무슨 요일 ? (SUN ,MON ...,SAT) 으로 return

# 문제 풀이 순서

# 1. datetime 을 import 한다
# 2. list 형태로 "MON" , "TUE" ... ,SUN 으로 만들어준다.
# 3. datetime.date().weekday 를 사용후 dictionary 에서 참조해 return

import datetime as dt


def solution(a, b):

    answer = ""
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    for i, j in enumerate(week):
        if dt.date(2016, a, b).weekday() == i:
            answer += j

    return answer


# print(dt.date(2016, 9, 6).weekday())
# - > 0 이 나오면 월요일 , 1 이 나오면 화요일 ..... 6이 나오면 일요일
# 0 ~ 6 을 보여줌
# week = ["MON", "TUE", "WED", "TUE", "FRI", "SAT", "SUN"]
# for i, j in enumerate(week):
#     print(j)

print(solution(5, 24))
