import numpy


def solution(scores):
    answer = ''
    temp_a = []
    temp_b = []

    get_num = 0

    for _ in range(len(scores)):
        temp_a.append([])

    for score in scores:
        for i in range(len(score)):
            temp_a[i].append(score[i])

    for div_score in temp_a:
        print(div_score)

        if div_score[get_num] == max(div_score) or div_score[get_num] == min(div_score):
            if len([i for i, ele in enumerate(div_score) if ele == div_score[get_num]]) <= 1:
                div_score.pop(get_num)
        temp_b.append((sum(div_score) / len(div_score)))
        get_num += 1
    for avg in temp_b:
        if avg >= 90:
            answer += "A"
        elif avg < 90 and avg >= 80:
            answer += "B"
        elif avg < 80 and avg >= 70:
            answer += "C"
        elif avg < 70 and avg >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))


def practice(something):

    for some in something:
        if some == 1:
            print(something.index(some))

    return True


a = [1, 1, 2, 3, 4]


b = [i for i, ele in enumerate(a) if ele == 1]

print(b)
