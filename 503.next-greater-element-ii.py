#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circular_nums=nums*2
        stk=[]
        l=len(nums)
        n=len(circular_nums)
        out=[-1]*n
        for i in range(n-1,-1,-1):
            while stk and stk[-1]<=circular_nums[i]:
                stk.pop()
            if stk:
                out[i]=stk[-1]
            stk.append(circular_nums[i])
        return out[:l]
        
# @lc code=end

