class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # so does not have to be ordered and just needs to be a sequence of 1 greater than the other for the longest amount. So largely speaking a primitive approach could be first sort the array. and then iterate through the arrays elements while keeping a count for the largest consecutive sequence. that would be solely dependent on the sorting algorithm. Another potential solution no matter what we have to check each element to ensure a consecutive sequence and also what about elements that are the same? I guess in that case we can take a unique set to mitigate that edge case. The contraints are large and can be almost any number. So this means that I should take a algorithm that should be around O(n) time. I for now cannot think of a more efficient method to do this. We need to take the first value as a starting point and now the length of the longest sequence is 1. Then from there we go to the next element and if current - previous is equal to 1 then we add 1 to the sequence otherwise we turn the current sequence to 1 and we need a continuous check at each element if the current sequence greater than the longest sequence. Instead of this an alternative solution is thus that we conver the array into a set. Then we start at each number and we check if the value +1 is inside the set. If not we simply move on but if so we add to the values for the current sequence and if thats longer than longest then we swap finally we return the longest sequence. To not repeat values we can do a seen value set. We start in the set we check if its in seen if not we create the next value and check if in if it is we add 1 and add both values to seen then continue to iterate until there is no value+1 and then we move on to next starting value and if seen we simply pass and move to the next value.
        longestSequence = 0
        
        numSet = set(nums)

        for num in numSet:
            if num-1 in numSet:
                continue
            
            currentSequence = 1
            curVal = num

            while curVal+1 in numSet:
                curVal+=1
                currentSequence+=1
            
            longestSequence = max(longestSequence, currentSequence)
        return longestSequence
            