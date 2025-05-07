class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0] # keeps track of our current buy price
        profit=0 # what our profit is so far

        for i in range(1, len(prices)): # single for loop to iterate through list of prices
            if (prices[i]<buy): #if we find a new cheaper buy price we can simply swap to the next price so no need to check every possible price
                buy=prices[i]
            elif(prices[i]-buy>profit): # and if that new price brings in a larger profit we swap the profit as well to show we found a new greatest profit
                profit=prices[i]-buy

        return profit # returns an integer of the profit 
    # performance is 31ms and beats 87.45% while taking 26.85mb of memory beating 78.00% of people
    # takes advantage of kadanes algorithm to do a single iteration
    # results in O(n) performance
    # checking every result was my initial approach but that was taking to long for large data sets.