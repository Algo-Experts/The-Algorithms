# Prices 가 매개변수로 주어질때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return

# def solution(prices):
#     answer = []

#     while len(prices) > 0:
#         now_price = prices.pop(0)
#         count = 0

#         for compare_price in prices:
#             if now_price <= compare_price:
#                 count += 1
#         answer.append(count)

#     return answer

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


print(solution([5, 4, 6, 2, 10, 13]))
