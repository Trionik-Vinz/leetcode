class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        left, right = 0, len(nums) - 1
        final_idx = -1

        l = 0
        r = 2
        m = 3
        f = 3
        [1,2,3,4,5,10]
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1
                final_idx = mid
                
            else:
                left = mid + 1
                final_idx = mid + 1
            
            #if right - left == 1:
            #    return final_idx

        return left
            
        