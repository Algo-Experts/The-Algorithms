# 문제 설명
# 0 ->  zero ... 9 -> nine
# "one4seveneight" 로 param s 가 들어왔다면, 해당하는 영문을 숫자로 바꿔서 return 하면된다.


# 풀이 순서
# 1. 영어를 일일이 리스트에 넣어준다 -> 이때 해당하는 원소의 번호에 해당 하는 것이 숫자가 된다.
# 2. enumerate 를 사용해서 dictionary 를 만들어준다.

def solution(s):

    num_en = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']

    for num, num_e in enumerate(num_en):
        if num_e in s:
            s = s.replace(num_e, str(num))

    return int(s)


# enumerate 롸?

num_en = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

dic = list(enumerate(num_en))

for i in range(len(dic)):
    print(dic[i])

# 출력 결과는
# (0, 'zero')
# (1, 'one')
# (2, 'two')
# (3, 'three')
# (4, 'four')
# (5, 'five')
# (6, 'six')
# (7, 'seven')
# (8, 'eight')
# (9, 'nine')
