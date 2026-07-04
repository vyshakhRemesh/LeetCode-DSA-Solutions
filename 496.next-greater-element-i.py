#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk=[]
        n=len(nums2)
        out=[-1]*n
        res=[]
        mapp={}
        for i in range(n-1,-1,-1):
            while stk and stk[-1]<nums2[i]:
                stk.pop()
            if stk:
                out[i]=stk[-1]
            if nums2[i] in nums1:
                mapp[nums2[i]]=out[i]
        
            stk.append(nums2[i])
        for n in nums1:
            if n in mapp:
                res.append(mapp[n])
        return res



        
# @lc code=end

