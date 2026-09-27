class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # so in this problem I need to take the number i start with and fill it with the product of all numbers that do not include it. So what might this look like? if im at index 0 for [1,2,4,6] the product for index 0 would be 2 x 4 x 6 being 48 and that would fill the index 0. So my intuition for this is I could take the value and then iterate across the array to all other elements not including it and multiply. This would be a O(n^2) solution. Not super viable. For my first pass through I could get 48 but for the next value I can divide by the index and then multiply everything before the index. In the solution we want to take a prefix from left to right multiplication array and a right to left post fix array and then multiply the right and left values of the index we are at together to get the array resulting in a O(n) solution.

        prefix=[nums[0]]
        postfix=[0]*len(nums)
        postfix[len(nums)-1] = nums[len(nums)-1] 
        n=1
        i=len(nums)-2
        productExceptSelf = []
        while n < len(nums):
            prefix.append(nums[n]*prefix[n-1])
            n+=1
        
        while i >= 0:
            postfix[i]=nums[i]*postfix[i+1]
            i-=1

        for j in range(len(nums)):
            left = prefix[j-1] if j>0 else 1
            right = postfix[j+1] if j<len(nums)-1 else 1
            productExceptSelf.append(left*right)
        return productExceptSelf