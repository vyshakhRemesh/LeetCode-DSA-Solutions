#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt=0

        # for i in range(1,x+1):
        #     if i*i<=x:
        #         sqrt=i
        # return sqrt

        left,right=1,x
        
        while(left<=right):
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            elif mid*mid>x:
                right=mid-1
        return right

# @lc code=end

