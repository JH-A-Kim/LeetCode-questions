class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # So we have a sorted array that we need to find the 2 numbers that add up to a target number. And we have to return the indices of 2 numbers such that they add up to the target and index1 < index2 and they cannot be equal. Always ine valid solution. And we need to do this is place. So what does this look like using the original solution it would be O(n) O(n) for space and time complexity so we need a new approach. This should come about in our sorted property in increasing order. Now what avenues could this take? We could maybe use binary search on the array to get a potential target value from the input because if the beginning is going up we can iterate as we go through. So lets say we start with 1 and then we binary search for the element that is target - current. and then we continue to iterate if not. That would be something like O(nlogn). O(1) memory. Ignoring this we can take the 2 pointer approach. If the numbers[0] + numbers[n-1] > target then we can numbers[n-2] and if the numbers[0] + numbers[n-1] < target then we can do numbers[0+1]+numbers[n-1]

        n = len(numbers)

        small = 0
        big = n-1

        while small != big:
            summed = numbers[small]+numbers[big]
            
            if summed == target:
                return [small+1, big+1]
            elif summed > target:
                big-=1
            elif summed < target:
                small+=1


