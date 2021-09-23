from collections import deque


def solution(priorities, location):
    answer = 0
    check = deque([0]) * len(priorities)
    priorities = deque(priorities)
    check[location] = 1
    while True:
        important = max(priorities)
        priorities_front = priorities.popleft()
        check_front = check.popleft()
        if priorities_front == important:
            answer += 1
            if check_front == 1:
                break
        else:
            priorities.append(priorities_front)
            check.append(check_front)

    return answer
