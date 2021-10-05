# 풀이과정
# 예시에 따라서 progresses 라는 배열에 순서대로
# 93 , 30 , 55 라는 배열이 주어 졌을경우,
# speed 의 배열의 수 1 , 30 , 5 에 따라
# 수가 증가 한다. 배열의 순서가 상관이 있으며,
# progresses 라는 배열에 따라 0번째 수가 100 이 되기 전까지는 두번째 작업의 진행이 불가 하다.
# 따라서 answer 의 배열에는 처음 100 이 된 기준의 날짜로, 완성된 기능의 수를 넣으면 된다.

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) != 0:
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
