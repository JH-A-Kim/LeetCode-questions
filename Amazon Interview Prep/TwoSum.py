class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values={} #empty dictionary to hold the indexes and indices

        for i in range(len(nums)): #we iterate through and make the values of the array the keys and values the indices for O(n) search time
            values[nums[i]]=i #reverse implementation of values
        for j in range(len(nums)): #single for loop for checking values
            diff=target-nums[j] #the value to search for in dictionary
            if diff in values and j!=values[diff]: #searches for value in dictionary while also checking if it is not just the same value as itself by checking if indices are same
                return [j, values[diff]] # returns the indices of it.
        