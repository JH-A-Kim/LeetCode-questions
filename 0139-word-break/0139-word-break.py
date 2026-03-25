class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # if a input word can be segmented at any point to make it so all words in the string exist in the dictionary then we can return true else false. So how can we break this problem down? For the time being we can look at maybe finding exists so if word in dict exists than return true. But that would fail to find multiple occurences and check other conditions so this would be insufficient. Another way i can think of is through iterating through the string slowly building and if at anypoint the string equals a word in the dict we vacate the holder string and then start again from the next character eventually checking until the end and if the holder string still contains letters then we return false. This would be O(n) for the iterating through the string and would maintain that as search in a dict is O(1). This solution is greedy and does not work. The real solution is by manually iterating through each and every part with an O(n^2) solution. we create a algorithm with the j and we only iterate when j's are valid and true so only when we reach valid points can we start to check we basically start from j->i see what happens. If dp[j] is not true we dont even look because that means from j there is no valid part inside the dict. And then we can check from each piece where their are valid sections in word dict for every possible combination until eventually we reach n and if dp[n] changes to true we return that.
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]