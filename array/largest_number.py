class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            li, ri = 0, 0

            while li < len(left) and ri < len(right):
                # modifies comparison step on mergesort
                a = str(left[li]) + str(right[ri])
                b = str(right[ri]) + str(left[li])

                if int(a) > int(b):
                    result.append(left[li])
                    li += 1
                else:
                    result.append(right[ri])
                    ri += 1

            if li < len(left):
                result.extend(left[li:])

            if ri < len(right):
                result.extend(right[ri:])

            return result

        def mergesort(nums: List[int]) -> List[int]:
            if len(nums) == 1:
                return nums

            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])

            return merge(left, right)

        result = ''.join([str(x) for x in mergesort(nums)])

        return result if result[0] != "0" else "0"
