def solution(people, limit):
    people = sorted(people)
    answer = 0
    start_index = 0
    last_index = len(people) - 1

    while start_index <= last_index:
        answer += 1
        if start_index >= last_index:
            break
        elif people[start_index] + people[last_index] <= limit:
            start_index += 1
        last_index -= 1
    return answer
