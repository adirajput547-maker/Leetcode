import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        h=[]
        for i in stones:
            heapq.heappush(h,-i)
        while len(h)>1:
            x=-heapq.heappop(h)
            y=-heapq.heappop(h)
            if x!=y:
                heapq.heappush(h,y-x)
        if h:
            return -h[0]
        else:
            return 0