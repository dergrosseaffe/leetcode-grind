class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # break into two groups for left and right products
        left    = [1] * length
        right   = [1] * length
        product = [1] * length

        p = 1
        for i in range(1, length):
            p *= nums[i - 1]
            left[i] = p
        print(left)

        p = 1
        for i in range(length - 1 - 1, -1, -1):
            p *= nums[i + 1]
            right[i] = p

        for i in range(len(nums)):
            product[i] = left[i] * right[i]

        return product
