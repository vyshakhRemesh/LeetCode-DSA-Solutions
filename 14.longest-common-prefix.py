#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        
        # Go through each character position of the first string
        for i in range(len(first_str)):
            char = first_str[i]
            
            # Compare this character with the same position in all other strings
            for other_str in strs[1:]:
                # If the other string is shorter than 'i', or the character doesn't match
                if i == len(other_str) or other_str[i] != char:
                    # Return everything we've matched up to this point
                    return first_str[:i]
                    
        return first_str
        
# @lc code=end

