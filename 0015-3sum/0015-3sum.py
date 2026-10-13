class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want a set of numbers that when added together they equate to 0. We want each distinct version of it. No implication there has to be one. So how might we go about this? A rudimentary approach is O(n^3) where we iterate through each element of the array one by one to get the solution. This is inoptimal for the number of values being up to 3000. Where else can we find optimizations. This could look like maybe a set? where we take each value put into a set. What if we take a pointer approach? We have 3 pointers we first sort the array. And then we iterate if sum > 0 we can move it back but then what do we do about the center value? This approach could make sense if we had a better iterating strategy. Then what else can we do? No we can iterate through each element. And then use that as the center point and then spread out with 2 pointers from the center. edge cases would have to be the left most element is i and the right most element is i. And then we simply go sum>0 element goes back one sum < 0 value goes up one. And then we simply check each element for the possibility of a triplet. resulting in O(n^2)

        triplets = []

        nums.sort()

        n = len(nums)

        for i in range(n-2):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, n-1

            while left < right:
                sumNum = nums[i]+nums[left]+nums[right]

                if sumNum < 0:
                    left+=1
                elif sumNum > 0:
                    right-=1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
        return triplets       