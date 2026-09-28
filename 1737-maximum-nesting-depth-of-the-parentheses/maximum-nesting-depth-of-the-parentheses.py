class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        stk=[]
        for i in s:
            if i=="(":
                stk.append(i)
            elif i==")":
                stk.pop()
            ans=max(ans,len(stk))
        return ans