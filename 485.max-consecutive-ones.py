#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum=0
        curr_count=0
        
        for i in nums:
            if i==1:
                curr_count+=1
                
            else:
                max_sum=max(max_sum,curr_count)
                curr_count=0
        
        return max(max_sum,curr_count)
        
# @lc code=end

