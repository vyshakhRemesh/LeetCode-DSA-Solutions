#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for i in operations:
            if i == "C":
                stk.pop()
            elif i == "D":
                stk.append(stk[-1]*2)
            elif i == "+":
                a=int(stk[-1])
                b=int(stk[-2])
                # a=stk.pop()
                # b=stk.pop()
                stk.append(a+b)
            else:
                stk.append(int(i))
        return sum(stk)
        
# @lc code=end

