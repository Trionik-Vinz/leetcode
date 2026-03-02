class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        result = 0
        n = len(s)
        for i in range(n):
            if n - 1 > i and letters[s[i+1]] > letters[s[i]]:
                result -= letters[s[i]]

            else:
                result += letters[s[i]]
        return result



        