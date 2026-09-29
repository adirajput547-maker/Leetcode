class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        while len(stones)>1:
            x=stones.pop()
            y=stones.pop()
            if x!=y:
                stones.append(x-y)
                stones.sort()
        if stones:
            return stones[0]
        else:
            return 0