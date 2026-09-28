class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h=nums[:k]
        heapq.heapify(h)
        for i in nums[k:]:
            if i>h[0]:
                heapq.heappop(h)
                heapq.heappush(h,i)
        return h[0] 