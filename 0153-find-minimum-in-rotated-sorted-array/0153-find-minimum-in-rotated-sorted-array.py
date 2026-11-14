class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Rotation just means everything moved down and around the array. We dont know the number of rotations. So we cant use an index. The values are not sequential so they dont go up by one. a rudimentary solution is just doing a regular min search which is O(n) time. We need something that runs in O(logn) time. Maybe if I look for another value first. No that wouldnt work. If i just tried a binary search it would quickly put me in the wrong place. I could look for the point at which they are no longer sorted. And then split the arrays and take the first value of the smaller array. The deflection point is the point where the value becomes smaller rather than bigger. And from there we simply take the min of the 2 arrays first index. 
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if  nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        # So once the loop ends l == r therefore the value has converged at the point where the previous value is greater than it and the proceeding value is greater than it. Its the value where everything before and after is bigger
