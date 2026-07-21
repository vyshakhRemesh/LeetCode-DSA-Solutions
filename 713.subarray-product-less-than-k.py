#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        pro=1
        count=0
        l=len(nums)
        if k<=1:
            return 0
        for right in range(l):
            pro*=nums[right]
            while pro>=k:
                pro//=nums[left]
                left+=1
            count+=right-left+1
        return count
        
# @lc code=end

