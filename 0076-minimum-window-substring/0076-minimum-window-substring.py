class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ok so i need to find the smallest substring that contains the characters in t. It needs to return a output string that is the window. How would i approach this? well first off its a window question. the window is dynamic and we need to keep track of everything in the window. So i can use the set counter as a way to keep track of the number of characters in the window. The important thing is knowing when to move. The way that i see it is the moment i find one character from t i put the start point there and then iterate until i find each character. If the starting character I find a duplicate more than needed in my set count of the window then i move the left most pointer forward to the left most indexed value inside the t set. Theoretically this should be O(nxm) where n is the size of s and m is the size of t because we have to put the t into a counter set and n needs to be iterated through. and then we simply return the string from index left to right. I also need to find a way to keep track of indexes of values. So maybe I could input the character into the set as an array that contains the count and index value. We need a validity check. If the string is valid we check if its the smallest we have seen if yes we update the min value and then we decrease its size on whatever maintains validity. 
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            # So TLDR what is this because i did not solve on my own. Right side will always expand and left side will get bigger or smaller based on validity of the window. So we use have as a way to keep track of how many conditions have been fulfilled and need as the total amount of conditions we need ie characters or versions of the actual characters with the numbers and the moment we reach have == need we check if the current len is less than the one we have save if so we save the subset and len and then we try shrinking using the left pointer and see if its still valid if so we repeat by -1 from have and then we keep moving forward if we still meet the condition we move the left pointer up. and then at the end of the loop we save res values to l, r and then we return that substring and if not we simply return ""

            