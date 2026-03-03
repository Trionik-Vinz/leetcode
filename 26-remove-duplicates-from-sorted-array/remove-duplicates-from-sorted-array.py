class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0: return 0  # Handle empty list
        if n == 1: return 1

        i = 0
        j = i + 1
        
        while j < n:
            if nums[j] != nums[i]:
                i += 1  # Increment i to the next slot
                nums[i] = nums[j]  # Move the unique element up
            j += 1  # Always increment j to scan the list
            
        return i + 1