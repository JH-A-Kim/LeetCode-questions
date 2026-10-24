class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation in string 2 strings s1 and s2. Return true if the second string contains a permutation of the first string and false otherwise. is this not just a sliding window question. Wait no its about the right number of characters not about a contiguous sequence of characters. I feel like we only really have to count the number of characters in the string in a set we iterate through and remove whatever characters from the first set for counts and then simply check if anything is 1 or greater in the first set and then simply return true for that or false. This kind of solution would be around O(3n) taking that down to O(n). memory would be O(1) because its a flat 26 potential characters. I need to consider negative values. i was on a wrong assumption it does have to be a contiguous secquence. Therefore I do need to use a sliding window. I feel that the inclusion set i can keep and then i know the size of my window and the characters so i can get that. And then i start at the beginning, count the characters inside and if the count matches we return true if not return false this would be O(nxm) where n is the size of s1 m is the size of s2 
        if len(s1)>len(s2):
            return False
        inclusionSet = defaultdict(int)
        subSet = defaultdict(int)
        r = len(s1)
        l = 0

        for c in s1:
            inclusionSet[c] += 1

        for i in range(r):
            subSet[s2[i]] += 1  

        while r < len(s2):
            if inclusionSet == subSet:
                return True
            
            subSet[s2[l]]-=1
            if subSet[s2[l]] == 0:
                subSet.pop(s2[l], None)
            l+=1
            subSet[s2[r]]+=1
            r+=1
        return subSet == inclusionSet

        