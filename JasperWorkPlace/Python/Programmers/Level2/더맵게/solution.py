import heapq


def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h)+(heapq.heappop(h)*2))
        except IndexError:
            return -1
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
