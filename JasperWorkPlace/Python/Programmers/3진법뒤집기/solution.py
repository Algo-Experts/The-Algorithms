# 짧은 문제

# 자연수 n 이 param 으로 , n을 3진법 상에서 앞뒤로 뒤집은 뒤에 이를 다시 10진법으로 return

# 문제 풀이 순서
#  1. 수를 뒤집어야 하기 때문에, String 변수 하나 생성
#  2. n 을 나눈 나머지로 3진법 String 변수에 차례로 저장 -> 먼저 들어간것이 숫자의 앞쪽으로 들어가므로, 따로 뒤집을 필요 없음
#  -- 추가
#  2-1. 마지막 나머지를 더해주어야지 full 로 3진법을 완성 가능

#  3. 나온 String 값을 차례로 3의 제곱순으로 더해줌


def solution(n):
    answer = 0
    #  풀이순서 1
    number = ""

    #  풀이순서 2
    while(n >= 3):
        number += str(n % 3)
        n = n//3
    #  풀이순서 2-1
    number += str(n)

    #  풀이 순서 3
    for i in range(0, len(number)):
        print(number[i])
        answer += int(number[i]) * int(3**((len(number)-1) - i))

    return answer
