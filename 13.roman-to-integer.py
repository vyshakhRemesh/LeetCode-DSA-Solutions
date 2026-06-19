#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hmap={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum=0
        for i,j in enumerate(s):
            sum+=hmap[j]
            if i!=0 and hmap[s[i]]>hmap[s[i-1]]:
                sum-=2*hmap[s[i-1]]
        return sum
        
# @lc code=end

