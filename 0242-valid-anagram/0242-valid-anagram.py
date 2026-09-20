class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # so we have 2 strings and if they are anagrams meaning they are can spell each other out. What this is basically checking is if there is the same number of each value in a string. So my basic intuition is that we iterate through one string and take note of the number of each value and compare the numbers against each other. so for example in racecar and carrace i see r=1 i check carrace set and see r is also = to 1 therefore i move forward. and continuing on until i either find one that is not or one that is. My solution is O(2N) How can I optimize? I could do an early check for size if not same size return false and then instead of iterating on the elements iterate using an index so i can cut out one of the for loops making it O(N) could also reduce it to one hash map by instead of using 2 doing a + - system where in the last check we just check if all values are zero. If not return false if yes return true. 
        string1 = {}
        string2 = {}
        for letter in s:
            if letter not in string1:
                string1[letter]=1
            else:
                string1[letter]+=1
        
        for letter in t:
            if letter not in string2:
                string2[letter]=1
            else:
                string2[letter]+=1

        return string1 == string2
        