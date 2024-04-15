class Solution:

    def __init__(self, w: List[int]):
        self.weights = [0]
        for weight in w:
            self.weights.append(self.weights[-1] + weight)
        self.upper_bound = self.weights[-1]


    def pickIndex(self) -> int:
        r = random.randint(1, self.upper_bound)

        left, right = 0, len(self.weights) - 1
        while left < right:
            mid = left + (right - left)//2

            if r == self.weights[mid]:
                return mid - 1
            elif r > self.weights[mid]:
                left = mid + 1
            else:
                right = mid

        return left - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()