class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
                # piles that is an array of integers where piles[i] is the number of bananas in the ith pile. Also have h which represents the number of hours to eat all said bananas. bananas per hour eating rate of k. We need to find the smallest version of k such that we can eat all bananas within h hours. We cannot use the k to eat more from another pile if we finish. We need to consider the edge case where we cannot each all the bananas as perhaps -1. So a rudimentary approach is finding the largest value pile. Iterate through see if everything in the array is 0 then we can return that as a potential solution then do k-1 and then repeat until we cannot. This would be O(n^h). This is certainly not the most performant solution. We need a better approach. So in what ways can we prevent repeated work while also keeping track of the values. Functionally it doesnt really matter the order of the piles. So we could reorganize it. we can take the largest value and simply do (x / k) if this is greater than h we move down else we save a potential min solution. where k starts off as the value x. And continually iterates down. Until x/k greater than h. This would be o(n+x). Using this logic I could take 4/4 = 1 1 is <9 so we continue and remove 1 4/3 take the ceiling and that is 2. and it is still < 9 we take 4/2 = 2 still less than 9. oh nevermind im assuming here that one pass through im eating that many bananas at each step not that each step takes that many bananas at each pile. But still it stands that the greatest element is our upper bound. So instead we take the upperbound we create an array from 1 to that element and then we binary search and do the computation. for hours if it is possible in that number of hours then we decrease the middle value otherwise we increase. TLDR we are still computing total time at each stage its just that because we are strictly bounded we can binary search the numbers in the bounds for a faster more efficient solution where we save the smallest value. 
        l, r = 1, max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            
            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res