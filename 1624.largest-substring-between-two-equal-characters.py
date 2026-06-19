#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hmap={}
        max=-1
        for ind,i in enumerate(s):
            if i in hmap:
                out=ind-hmap[i]-1
                if out>max:
                    max=out
            else:
                hmap[i]=ind
        return max
        
# @lc code=end

