from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given a string s only uppercase english characters and integer k we can take up to k characters and replace them with another uppercase english character. We are aiming to create the longest substring of one character. we are looking for a window of size k+2 or smaller that can be replaced with a single letter such that it creates the longest substring of a single character. First of all how do we determine the character? maybe we move the window forward until we find a start point and end point of size k that are both the same character. Then we can make the change for each value change it into the border characters and then simply iterate through it and count each value. Edge cases: what if its center focused like xyyx we would never get yyyy as a potential solution or in a bigger case xryyyxr where k=2 we would never get the case such that it becomes xyyyyyr. So maybe we find the longest contiguous substring and then add to its boundaries. TLDR yes it is a sliding window problem. Using a dynamic window where we increase the window size based on the contiguous chunks of same characters. where the window size is equivalent to the count of the most frequent character <= k why is that because the characters that are not the most frequent are the ones we need to replace. I can start with a value i increase the window up to k times where it wont count if we find a repeated value. Ok now I watched the video how do i understand this? Basically we take a sliding window approach where we take a count of the number of each character into account as we move we update this count of characters. The condition for moving the dynamic window size is for the window to be valid. Validity is dictated by the length of the window - highest frequency character count <= k because that is the number of replacements we can do. If this no longer becomes valid we move the left pointer forward and start the process again. Eventually this will result in the window being the longest repeating character replacement subarray. We also need to keep track of a result length. TLDR we for loop on r and we simply move the left pointer anytime we dont have a valid window and then we move it remove one from the char count and then keep on going till valid and we take the res at the end as max. 

        l = 0
        r = 0
        res = 0
        charCount = defaultdict(int)

        for r in range(len(s)):
            charCount[s[r]]+=1

            while r-l+1 - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1)
        
        return res

            
            
            