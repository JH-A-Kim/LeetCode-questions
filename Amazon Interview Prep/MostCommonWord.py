import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        newP=paragraph.lower() #sends to lower
        cleaned=re.sub(r"[,.;@#?!&$']", " ", newP) #replaces all punctuation with white spaces
        newList=cleaned.split() #splits all the values into an array
        words={} #words to keep track of length of values
        bannedWords={} #words that are banned dictionary for O(1) access

        maximum=0 #keeps track of largest number of occurences
        word="" #keeps track of the actual word

        for i in banned: #builds the banned dictionary where the keys are the words themselves
            bannedWords[i]=1

        for i in newList: #builds the words dictionary keeping track of occurences of certain values that are not in banned
            if (i in words and i not in bannedWords):
                words[i]=words[i]+1
            elif (i not in words and i not in bannedWords):
                words[i]=1
        
        for i in words: #gets our largest number of occurences word
            if(words[i]>maximum):
                maximum=words[i]
                word=i
        return word
    
    #executes in O(n) time with 0 ms beating 100% and 17.65 mb of memory to beat 94.7% in memory efficiency

        