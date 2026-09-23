class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so we have a group of strings and we need to check whcih values are anagrams ie meaning they contain the same number of values and they are the same values. A rudimentary approach sees this as we take each string we turn it into a hash set and then do the same with each str and then compare against each hash and then group the sets and return the array. This would be roughly O(n^2). SO tldr for most optimal solution we set up a list dictionary, we then iterate through the strings with a array count of 26 0's from there we iterate through the characters in the string. from there we get the number of each character instance into the array and from there we use the count as an key made as a tuple and add the string to the list. and then we simply return the hash set. SO after completing this problem what did I learn? I learned that defaultdict will automatically start anything that is not already in the set as a empty list when i get a new key. I found that ord turns each character into its numeric ascii value a value multiplied by a array converts it into that many elements, and tuple will convert a value into a basically unchanging list and .values() gives you just the values in a set and then list converts them all into a list. basically the intuition is that we can convert each value into a tuple that holds their exact amount of values. And then create a key in a hash set that we can add to using each value as a key allowing it to be O(n*m) where n is the number of strings and m is the number of characters. 

        anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # this is to make an array with 26 characters
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())