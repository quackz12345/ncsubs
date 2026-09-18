class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sum = 0
        ans = len(nums)+1

        for right in range(len(nums)):
            sum += nums[right]

            while sum - nums[left] >= target:
                # remove arr[left] from curr
                sum -= nums[left]
                left += 1
                

            if sum >= target:
                ans = min(ans, right-left+1)
        
        return 0 if ans == (len(nums)+1) else ans