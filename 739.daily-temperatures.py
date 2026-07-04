#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        n=len(temperatures)
        out=[0]*n
        c=0
        for i in range(n-1,-1,-1):
            while stk and temperatures[i]>=temperatures[stk[-1]]:
                stk.pop()
                
            if stk:
                out[i]=stk[-1]-i
                
            stk.append(i)
        return out
        
# @lc code=end

