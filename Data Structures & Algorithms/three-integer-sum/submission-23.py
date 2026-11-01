class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        rr = len(nums) - 1

        while rr >= 2:
            if rr < len(nums) - 1 and nums[rr] == nums[rr + 1]:
                rr -= 1
                continue

            if nums[rr] < 0:
                break

            l = 0
            r = rr - 1

            while l < r:
                total = nums[l] + nums[r] + nums[rr]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[l], nums[r], nums[rr]])
                    left_value = nums[l]
                    right_value = nums[r]

                    while l < r and nums[l] == left_value:
                        l += 1
                    while l < r and nums[r] == right_value:
                        r -= 1

            rr -= 1

        return ans