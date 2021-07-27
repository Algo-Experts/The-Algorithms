def solution(phone_number):
    answer = ''

    new_array = list(phone_number)
    i = len(new_array) * (-1)

    while i < 0:
        if i < -4:
            new_array[i] = "*"
            answer += new_array[i]
            i += 1
        else:
            answer += new_array[i]
            i += 1

    return answer


phone = "022224443"

print(solution(phone))
