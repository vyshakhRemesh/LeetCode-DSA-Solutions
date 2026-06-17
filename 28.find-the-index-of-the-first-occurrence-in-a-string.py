#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        # Slide a window of length len(needle) across haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the current substring matches the needle
            if haystack[i : i + len(needle)] == needle:
                return i
                
        return -1
        
# @lc code=end

