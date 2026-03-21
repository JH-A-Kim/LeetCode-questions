class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, L, R): # expand function will expand around center by taking a left and right input start as well as a string. After that it checks using odd logic and left logic from the inputs. it does a while loop from the center and the moment things do not equal it will return the substring palindrome
            while L >=0 and R < len(s) and s[L] == s[R]:
                L-=1
                R+=1
            return s[L+1 : R]

        best = ""

        for i in range(len(s)): ## after we return the substring palindromes for each value in the array moving from the center we simply check which substring is bigger than best. This overall is an application of 2 pointer but from the inside out not the outside in.
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even

        return best
        
                
