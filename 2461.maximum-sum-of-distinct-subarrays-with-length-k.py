#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        maxi=0
        n=len(nums)
        map={}
        for i in range(0,k):
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1
            sum+=nums[i]
        if len(map)==k:
            maxi=sum
        

        for j in range(k,n):
            sum+=nums[j]-nums[j-k]
            map[nums[j-k]]-=1
            if map[nums[j-k]]==0:
                map.pop(nums[j-k])
            if nums[j] in map:
                map[nums[j]]+=1
            else:
                map[nums[j]]=1
            if len(map)==k:
                maxi=max(maxi,sum)
        return maxi

        
# @lc code=end

