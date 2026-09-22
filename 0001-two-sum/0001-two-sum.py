class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # basically take the values at indices i and j where the number is equal to the input target and we cannot use the same index value. Every single input array will always have a pair that meets the condition. My basic intuition is that if we iterate through we check each value. With each value against the others and if we meet the target it returns the indices. This would be about O(n^2) for the double for loop. Potentially a better solution could use a set. we get each value in the set and if we do target - index is in the set we return the indices. We would need the set to hold the index. 11

        valueSet = {}

        for i in range(len(nums)):
            valueSet[nums[i]] = i
        
        for i in range(len(nums)):
            returnTest = target - nums[i]
            if returnTest in valueSet and valueSet[returnTest]!=i:
                return [i, valueSet[returnTest]]
            