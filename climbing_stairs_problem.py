class Solution(object):
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            step1 = 1
            step2 = 2
            if n == step1:
                return 1
            if n == step2:
                return 2
            else:
                return (self.climbStairs(n-1)+self.climbStairs(n-2))
        
