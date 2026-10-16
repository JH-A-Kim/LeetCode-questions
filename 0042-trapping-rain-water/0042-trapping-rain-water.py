class Solution:
    def trap(self, height: List[int]) -> int:
        # well i need to consider the total max i can fit between 2 sections considering their height. So potentially I have 2 spaces and inbetween these spaces there is heights that block and create space. Either way I need to find the maximum possible amount of water. From what I gather I need to find the heights of all values non zero and calculate the value between each non zero. For the left I would need to get the left height and right height and that gives me the space. But then in the middle i need to take the height of the left value and the right value and subtract the smaller heights from the total. and the edges dont count as heights to take space. And there must exist at least one empty space inbetween heights. 2 pointer approach
        left = 0
        right = len(height)-1

        if not height:
            return 0
        
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left<right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res