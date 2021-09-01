# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수,
# solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고,
# "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.


def solution(s):
    answer = ""
    arr1 = s.split(" ")
    new_array = []
    answer_array = []
    for i in range(len(arr1)):
        new_array.append(int(arr1[i]))

    answer_array.append(str(min(new_array)))
    answer_array.append(str(max(new_array)))

    answer = " ".join(answer_array)

    return answer


print(solution("-1 -1"))


s = "1 2 3 4"


def solution2(s):
    arr_s = list(map(int, s.split()))
    print(arr_s)


solution2(s)
