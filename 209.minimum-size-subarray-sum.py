#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        summ=0
        min_len=float('inf')
        l=len(nums)
        for right in range(l):
            summ+=nums[right]
            while(summ>=target):
                min_len=min(min_len,right-left+1)
                summ-=nums[left]
                left+=1
        return 0 if min_len == float('inf') else min_len
        
# @lc code=end

