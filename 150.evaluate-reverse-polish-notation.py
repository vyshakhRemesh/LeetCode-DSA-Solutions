#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for i,j in enumerate(tokens):
            if j!="+" and j!="-" and j!="*" and j!="/":
                stk.append(int(j))
            else:
                a=int(stk.pop())
                b=int(stk.pop())
                x=0
                if j=="+":
                    x=b+a
                elif j=="-":
                    x=b-a
                elif j=="*":
                    x=b*a
                elif j=="/":
                    x=int(b/a)
                stk.append(x)
        return stk[-1]

        
# @lc code=end

