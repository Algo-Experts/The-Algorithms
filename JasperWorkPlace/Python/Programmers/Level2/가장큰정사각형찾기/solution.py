# Dynamic Programming 이 필요한 문제!!

# 작은 정사각형부터 확인하고, 하나하나 키워나가면서 확인하는 문제, 즉 작은 정사각형부터 하나하나
# 값을 쌓아 나가면서 해를 구해야한다.

# 그게 아니라면, 3중 반복문을 사용해서 문제를 풀어나가야하는데, 파이썬이 1초당 2천만번 계산이 가능한것을 고려해봤을때,
# 5초 정도가 걸리는 것을 알 수 있다. ( 최대 행 열의 크기가  1000 3중 for loop -> 1000 ** 3)


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i-1][j], board[i]
                                  [j-1], board[i-1][j-1]) + 1
    return max([num for row in board for num in row]) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [
      1, 1, 1, 1], [0, 0, 1, 0]]))  # Expect 9
# print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
