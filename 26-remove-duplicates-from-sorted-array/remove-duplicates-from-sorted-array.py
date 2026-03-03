class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        freq_map = {}

        # Populate the frequency map with 0 as a placeholder
        for i in range(0, n):
            freq_map[nums[i]] = 0

        j = 0
        # Overwrite the original list with unique keys from the map
        for k in freq_map:
            nums[j] = k
            j += 1

        # Now return works because it is inside the function
        return j
      

        