class Solution:
    def maxArea(self, height: List[int]) -> int:
        # so what i need to find is the tallest but also has the furthest x axis length to create the greatest area between the 2 points. So i have to calculate the area based on the index of the left most line to the right most line looking like left-right is the length multiplied by the shorter of the 2 lines. So at each point in a initial solution i could take for each value calculate out each area from each starting point. That would result in a o(n^2) solution and as thebn could be 10^5 it would be difficult to really hold up. Now what would work better? we want to be able to take advantage of each property that stipulates some condition to reduced the amount of iterations therefore we could start off by finding the largest values in height and then calculating the distance between. But if i follow with 2 pointers i can start on the right and expand out for each element and keep a running total called largestArea. once the right one ends at the final part we can then take the left pointer and then calculate that as we move to the right. and then we just take max or just whatever is best. Thtat results in O(2n). This unfortunately did not work. What i really need to do is close the pointers closer and closer and as we move the shorter wall inward we have a chance to get a better wall or taller width. Whereas if we move the taller wall we are guarnteed equal or less than in terms of area. So this would be a O(n) solution

        n = len(height)

        left = 0
        right = n-1

        best = 0

        def area(height, left, right):
            smallWidth = min(height[left], height[right])
            length = right - left

            return smallWidth * length

        while left<right:
            areaOfSection = area(height, left, right)

            if best<areaOfSection:
                best = areaOfSection

            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1

            
        return best

