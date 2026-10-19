class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Best time to buy and sell a stock. We have a array prices where prices[i] is the price of a stock on the ith day. Can choose one day to buy and one day to sell. Return the max profit. Can also choose to do nothing for 0 profit. For a sub optimal solution we can simply count each outcome individually resulting in a O(n^2) solution. This is not optimal theoretically I could approach this with a 2 pointer approach but its not sorted so that would not help and moving the pointers just makes it O(n^2) anyways. So a sliding window can be a potential approach. No but there isnt anything to gate its size. If I keep track of the cheapest price so far and then test against each value proceeding if it has a higher sell price. TLDR is that we think about the values as we go. We keep a pointer at the smallest value we have seen so far and a max value counter we take the total max of whatever we have seen and leave the pointer at the smallest value we have seen so far. and then continue to iterate as this is basically us going in blind and keeping an eye on the left most small value. 
        maxP = 0
        minV = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minV)
            minV = min(minV, sell)

        return maxP
        