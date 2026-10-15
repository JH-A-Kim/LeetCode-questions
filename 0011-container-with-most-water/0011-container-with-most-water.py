class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # array heights where heights[i] is the height of the ith bar its literally just the height of the bar. We need to find a container size that holds the most amount of water. So not only do i need a large set of heights i need the most optimal length. Atomically this calculation is just the height of the shorter bar multiplied by the distance between the 2 bars. For example in the example height = [1,7,2,5,4,7,3,6] the most optimal is 7 and 6 there is 6 spaces between them so 6 x 6 results in 36. So this problem is 2 pronged finding the optimal heights and optimal distances. So starting with a potential intuition we can take the fact that it has high number of potential inputs as it needing something below O(n^2) time complexity. Therefore it should be something like O(n) or O(nlogn) so what can I infer from this? Maybe if i take a 2 pointer approach I can find the optimal value. But the problem quickly becomes that this is not sorted but if i find every combination that technically gives me the answer but that has high time complexity. Lets say I take the left most number and expand out. and see what would give me a higher value. and then move my right pointer. What if for every value I iterate and then i take a nested loop and iterate once for the right to find the best value. What if instead we took the values from both sides as pointers and calculate the value. We then decrement or increment whichever side has a lower height. the lower height is always the lower bound and it can change the outcome whereas changing the higher bound can never make the value bigger whereas changing the lower bound can make the value bigger or smaller. Real change happens on the lower value.

        left = 0
        right = len(heights)-1
        greatestArea = 0

        while left<right:
            area = (right - left) * min(heights[left], heights[right])
            
            if area > greatestArea:
                greatestArea = area

            if heights[left] > heights[right]:
                right-=1
            elif heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return greatestArea

