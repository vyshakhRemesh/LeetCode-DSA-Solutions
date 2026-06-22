#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stk=[]
        self.topVal=-1
        self.min=[]

        

    def push(self, value: int) -> None:
        self.stk.append(value)
        self.topVal+=1
        if not self.min:
            self.min.append(value)
        else:
            if self.min[-1]>value:
                self.min.append(value)
            else:
                self.min.append(self.min[-1])
        

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
            self.min.pop()
            self.topVal-=1
        

    def top(self) -> int:
        return self.stk[self.topVal]
        

    def getMin(self) -> int:
        return self.min[self.topVal]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.topVal()
# param_4 = obj.getMin()
# @lc code=end

