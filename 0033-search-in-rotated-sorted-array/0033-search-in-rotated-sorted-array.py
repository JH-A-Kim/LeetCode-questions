class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so the original find minimum was finding the break point when a value that is next to it is less than it. Using binary search. So how may we go about finding the value here? Potentially we can use the same principle we can find the middle point. And then we simply find the range of values if the target is within one of those ranges we take that array from which we split from and then simply binary search that. Otherwise return -1

        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                # if middle value greater than the right most value than we simply move the 
                l = m+1
            else:
                # if middle is less than right so we gotta move right down
                r = m
        # so now we have the deflection point we can either use l or right.
        pivot = l

        l, r = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
        