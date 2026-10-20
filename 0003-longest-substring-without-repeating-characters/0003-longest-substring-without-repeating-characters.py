class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i have a string s and i need to find the longest substring without duplicates. Substring is a contiguous sequence of characters within a string. Basically in its order so even if the value is zvbzsnx the longest is 4 and not zvbsnx which is 6. So what way can i tackle this problem. I can take the create a sliding window of values where it starts off. What if i take this with a stack no i cant do that because i dont know where the repeated character could be. A core problem is knowing whats inbetween each set of values. This means I could take a hash set for O(1) lookup as we iterate and take a sliding window approach where i start at the first value i keep on going. the moment I hit a repeated value i see if the total count is larger than the current max and if so simply replace the max. If not the hash has the index for the repeated character and then we start iterating from there +1. so theoretically i can go abcdefghijkalmnopqrstuvwxyz and i start at b going to the end as the total value. Edge cases empty string, all same characters. Dont want to repeat work so i can remove the old value replace it with the new value start there and do -1 to remove the value count and then simply continue without repeating work. 
        values = {}
        maxCount = 0
        left = 0
        for i in range(len(s)):
            if s[i] in values and values[s[i]] >= left: # this check also makes sure we dont go backwards to old indexes on previously moved past values. No repeated work. 
                left = values[s[i]]+1
            values[s[i]] = i
            maxCount = max(maxCount, i-left+1)
        return maxCount

# values={z:3, x:1, y:2}
# current = 3
# maxCount = 3
# values get left behind and not reset I need to figure out a way to remove all values before the repeated value. 
# tldr we take a left pointer value and we iterate through if we see a repeated value our left becomes that + 1 and then we simply replace the value in values set. From there we simply calculate from that left most value to the current iterated point what is the value and then that is our value at that iteration and then we take the max of that vs the total max. That gives us a dynamic way to update the max value as we go value by value without repeating work. 
