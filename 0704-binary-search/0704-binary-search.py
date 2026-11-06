class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so this is literally just binary search implementation which basically just has the stipulation that a array be sorted first and then we get the middle element we compare it to the target. If they equal we return that index if the value is less than the target than we focus on the right side. if the value is greater than the target than we focus on the left side. repeating with the middle value until we reach. This is O(logn) time because we are halving the space at each step. 
        l = 0
        r = len(nums) - 1 
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m]<target:
                l = m + 1
            else:
                r = m - 1
        return -1