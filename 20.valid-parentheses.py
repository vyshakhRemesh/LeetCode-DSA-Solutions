#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        checktrue={
            "{":"}",
            "(":")",
            "[":"]"
        }
        stack=[]
        for i in s:
            # print(i in checktrue)
            if i in checktrue:
                stack.append(i)
                # print(stack)
            
            else:
                if not stack:
                    return False
                # print(stack[-1])
                if checktrue[stack[-1]]==i:
                    stack.pop()
                    # print("after pop",stack)
                else:
                    return False
        # print(stack)
        # print(s)
        if len(stack)>0:
            return False
        else:
            return True

        
# @lc code=end

# obj=Solution()
# out=obj.isValid("(])")
# print(out)