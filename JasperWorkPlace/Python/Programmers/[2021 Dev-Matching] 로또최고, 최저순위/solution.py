#  일단 문제가 너무 길다..
#  1~45 까지의 숫자 6개 맞추기
#  1등 ~ 5등 6~2개 번호 일치
#  6등 탈락 // 갑지기 동생이 낙서 알아볼수 없는 숫자 = 0
#  민우가 44 1 0 0 31 25 일때 당첨번호 31 10 45 1 6 일때
#  두개의 0 이 10 혹은 6 일때 3등이 최고 최저는 5등
#  answer = [ 최고 순위  , 최저 순위]

#  <<문제 풀이 순서>>
#  1. 일단 배열 lottos에서 0의 갯수를 확인한다.
#  2. 0의 갯수 중에서 win_nums 가 몇개 있는지 확인한다
#  3. 그렇다면, 최댓값은 배열 속 0의 갯수가 모두 당첨번호라 가정 했을때 0의 갯수 + 안지워진 수 중에 당첨 번호 수
#  4. 최소값은 안지워진 수 중에 성공한의 수 (지워 진수 0은 모두 실패)
#  5. 6등 6등 5등 4등 3등 2등 1등 -> ranks 배열
#  6. 0개 1개 2개 3개 4개 5개 6개 -> 틀린 갯수


def solution(lottos, win_nums):

    # 5번, 6번 문제 풀이 순서
    ranks = [6, 6, 5, 4, 3, 2, 1]

    #  1번 문제 풀이 순서
    #  Using Count method for checking integer '0' in array
    a = lottos.count(0)

    # initialize for adding nums in Correct lottery num in win_nums
    b = 0

    # << 기초 다지기 >>
    # 자바와 비교 하여 파이썬의 for 문은
    # for(int i = 0 ; i < something ; i++)
    # 와 다르게 array 안의 원소를 a 라고 가정하고 for a in array:  라고 선언한다.
    #  a 가 별의미가 없을 경우 _ 로 initialize 한다.

    # 3 , 4 , 5 번 문제 풀이 순서
    for _ in win_nums:
        if _ in lottos:
            b += 1

    answer = [ranks[a+b], ranks[b]]

    return answer
