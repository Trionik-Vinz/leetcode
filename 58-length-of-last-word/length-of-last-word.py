class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # .split() without arguments automatically handles multiple 
        # spaces and removes leading/trailing whitespace.
        words = s.split()
        
        # If the string was just spaces, return 0 (though constraints say length >= 1)
        if not words:
            return 0
            
        # Return the length of the last element in the list
        return len(words[-1])