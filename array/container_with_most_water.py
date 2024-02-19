class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        volume = 0
        while (left != right):
            distance = abs(right - left)
            hl, hr = height[left], height[right]
            volume = max(volume, min(hl, hr)*distance)

            right -= 1 if hr < hl else 0
            left  += 1 if hl <= hr else 0

        return volume
