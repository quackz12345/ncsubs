class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = maxa = 0

        right = len(heights) - 1
        maxa = (right - left) * min(heights[right], heights[left])
        while left < right:
            # do some logic here with left and right
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            maxa = max(maxa, (right- left) * min(heights[right], heights[left]))

        return maxa
