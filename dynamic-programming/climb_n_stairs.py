class Solution:
    def climbStairs(self, n: int) -> int:
        computed = {}

        def climbNStairs(n: int) -> int:
            if n == 1: return 1
            if n == 2: return 2
            if n in computed:
                return computed[n]

            value = climbNStairs(n-1) + climbNStairs(n-2)
            computed[n] = value

            return value

        return climbNStairs(n)
