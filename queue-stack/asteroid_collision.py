class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # a collision will happen
            while stack and asteroid < 0 < stack[-1]:
                top = stack[-1]
                if top == -asteroid:    # both are same size
                    stack.pop()
                    break
                elif abs(top) > abs(asteroid):  # current asteroid in stack is bigger
                    break
                else:
                    stack.pop() # removes current asteroid in stack. will add asteroid on else
            else:
                stack.append(asteroid)

        return stack
