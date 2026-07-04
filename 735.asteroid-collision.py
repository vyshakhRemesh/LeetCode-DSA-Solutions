#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        out=[]
        for i in asteroids:
            collision=True
            if i>0:
                stk.append(i)
            elif i<0:
                while stk and stk[-1]>0:
                    if -1*i > stk[-1]:
                        stk.pop()
                    elif -1*i < stk[-1]:
                        collision=False
                        break
                    else:
                        stk.pop()
                        collision=False
                        break
                if collision:
                    stk.append(i)
        return stk
                        


        
# @lc code=end

