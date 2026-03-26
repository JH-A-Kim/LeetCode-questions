class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # general intuition I can look at this the way that i see it this will need 3 pointers. and will look at being around a o(n^3) solution due to that fact because in my initial intuition it will take iterating through n for every number and then every combo of n-1 and then n-2 resulting in O(n^3) solution for the initial solution. ut this is not viable because there could be up to 3000^3 size which would result in a sub optimal run time. If we fix one of these numbers it just results in 2 sum so we create that solution but for each value. So instead we can look at a O(n^2) 2 pointer approach. If we sort the array we can create predictable behaviour for iteration. so if we create for loop with a fixed set at each point and we check for each value and only iterate forward when it will impact the outcome we can check all reasonable checks while maintaining O(n^2) this comes from being sorted where if the total is less than 0 we can simply incriment the left pointer and otherwise increment the right pointer on the right side and if we do equal 0 we can simply append the value and check the other results by incrementing the left pointer. After that we simply check duplicates with it skipping duplicate values. 
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1

            while j<k:
                total = nums[i]+nums[k]+nums[j]

                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j+=1
        return res





        