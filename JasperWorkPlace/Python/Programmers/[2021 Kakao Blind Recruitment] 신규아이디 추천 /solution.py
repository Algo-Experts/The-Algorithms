# 문제 풀기

def solution(new_id):

    answer = ''

#   모든 문자를 소문자로 만든다
    new_id = new_id.lower()

#  isalnum 메소드는 true false 를 return 해주는데 직관적으로 모두 숫자인지 알파벳인지를 확인해준다.
    for word in new_id:
        if word.isalnum() or word in '._-':
            answer += word

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))

    return answer
