class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount=0
        def expand(string, L, R):
            count=0
            while L>=0 and R<len(string) and string[L]==string[R]:
                L-=1
                R+=1
                count+=1
            return count

        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            totalCount=totalCount+odd+even
        
        return totalCount
            