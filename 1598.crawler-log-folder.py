#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk=[]
        for i in logs:
            if i == "../":
                if stk:
                    stk.pop()
            elif i=="./":
                continue
            else:
                stk.append(i)
        return len(stk)
        
# @lc code=end

