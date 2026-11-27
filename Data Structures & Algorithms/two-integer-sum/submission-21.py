class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0
        seen = {}
        for x,xx in enumerate(nums):
            complement = target -xx
            if complement in seen:
                return [seen[complement],x]
            seen[xx] = x