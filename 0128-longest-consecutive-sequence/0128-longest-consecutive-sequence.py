class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # so does not have to be ordered and just needs to be a sequence of 1 greater than the other for the longest amount. So largely speaking a primitive approach could be first sort the array. and then iterate through the arrays elements while keeping a count for the largest consecutive sequence. that would be solely dependent on the sorting algorithm. Another potential solution no matter what we have to check each element to ensure a consecutive sequence and also what about elements that are the same? I guess in that case we can take a unique set to mitigate that edge case. The contraints are large and can be almost any number. So this means that I should take a algorithm that should be around O(n) time. I for now cannot think of a more efficient method to do this. We need to take the first value as a starting point and now the length of the longest sequence is 1. Then from there we go to the next element and if current - previous is equal to 1 then we add 1 to the sequence otherwise we turn the current sequence to 1 and we need a continuous check at each element if the current sequence greater than the longest sequence. 
        if not nums:
            return 0
        longestSequence = 1
        currentSequence = 1
        sortedArray = sorted(nums)

        for i in range(1, len(sortedArray)):
            diff = sortedArray[i] - sortedArray[i-1]
            if diff == 1:
                currentSequence +=1
            elif diff == 0:
                continue
            else:
                currentSequence = 1
            longestSequence = max(longestSequence, currentSequence)

        return longestSequence