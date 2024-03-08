class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        squares = [0] * len(nums)
        current = right

        while left <= right:
            if abs(nums[left]) > nums[right]:
                squares[current] = nums[left] ** 2
                left += 1
            else:
                squares[current] = nums[right] ** 2
                right -= 1
            current -= 1

        return squares
