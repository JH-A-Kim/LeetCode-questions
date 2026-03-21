class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, L, R):
            while L >=0 and R < len(s) and s[L] == s[R]:
                L-=1
                R+=1
            return s[L+1 : R]

        best = ""

        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even

        return best
                
