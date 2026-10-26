class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr = nums
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                # do something
                return mid
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # left is the insertion point
        return -1