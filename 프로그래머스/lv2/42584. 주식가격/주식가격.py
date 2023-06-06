import heapq


def solution(prices):
    n = len(prices)
    answer = [0] * n
    heap = []
    heapq.heappush(heap, [-prices[0], 0])
    for i in range(1, n):
        heapq.heappush(heap, [-prices[i], i])
        if -prices[i] > heap[0][0]:
            while -prices[i] > heap[0][0]:
                value, index = heapq.heappop(heap)
                answer[index] = i - index

    while len(heap) > 0:
        value, index = heapq.heappop(heap)
        answer[index] = n - 1 - index

    return answer