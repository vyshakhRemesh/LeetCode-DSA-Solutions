#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0
        max_len=0
        l=len(nums)
        left=0
        for right in range(l):
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                max_len=max(max_len,right-left+1)
        return max_len


        
# @lc code=end

