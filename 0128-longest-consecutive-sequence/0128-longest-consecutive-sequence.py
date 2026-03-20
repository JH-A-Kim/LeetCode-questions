class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        tempCount=1
        n = len(nums)

        print(nums)
        if not nums:
            return 0
        if n==1:
            return 1
        
        for index in range(1, n):
            diff = nums[index] - nums[index-1]
            if diff==1:
                tempCount+=1
                print("1")
            elif diff == 0:
                print("0")
                pass
            elif diff > 1 and count<tempCount:
                count = tempCount
                tempCount = 1
            else:
                tempCount = 1

        if count<tempCount:
            count=tempCount

        return count