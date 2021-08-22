#  생각 보다 까다로운 문제
# 2 차원 배열을 다루는 냄새가 난다.

# 문제 정리
# board param => [[0번째 줄 차있는 수]] , [1번째 줄 차있는 수] , [2번째 줄 차있는 수] , [3번째 줄 차있는 수]]
# moves param => [a,b,c,d,e] => a 번째 행에서 제일 위에 있는 인형 뽑고, ... 쭉 넘어간다.


# 문제 풀이 순서
# 1. 뽑은 인형을 넣어둘 배열을 생성 해준다.
# 2. ... 풀면서 정리 ...


def solution(board, moves):
    # 배열( 바구니 ) 생성 가지고 온 인형을 여기에다가 쌓는다.
    basket = []
    answer = 0

    # moves 배열안에 있는 원소의 위치 에서 인형을 들고온다,
    for move in moves:
        # 현재의 board 크기를 파악해서 크레인( 집게 )의 이동 수를 한정 해주고
        for i in range(len(board)):
            # board는 2차원 배열 이기 때문에  board[i][j] 의 형식으로 가지고 오는데 만약 0 이 아니면 바구니에 집어 넣고 해당 위치의 원소는
            # 0으로 만든다.
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0

                if len(basket) > 1:
                    # basket 안에 있는 연속되는 숫자(인형)이 있을시에
                    if basket[-1] == basket[-2]:
                        # basket 안에서 제거해준다.
                        basket.pop(-1)
                        basket.pop(-1)
                        # 터트려진 숫자(인형) 의 수를 answer에 더해준다.
                        answer += 2
                break
    return answer
