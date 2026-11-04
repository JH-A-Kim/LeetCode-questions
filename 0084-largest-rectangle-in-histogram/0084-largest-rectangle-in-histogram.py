class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # array of integers heights where heights[i] represents the height of a bar. The width is 1. Return the area of the largest rectangle among bars. So in what ways can i identify this. We would need to keep track of the smallest we add all values into the stack. we can then make groupings and pop in groups. Keep a stack of indices where the bar heights are in increasing order. As long as the next bar is taller or equal we keep pushing indices. When we see a shorter bar it means the bar on top of the stack cant extend further to the right. We pop and treat it as the height of a rectangle. Its width goes from the new top of the stack+1 up to the current index - 1. So tldr we do a pass through of the heights array where we add a value. If the next value is the same height or larger we add it to the stack. once we reach a value that is less than the current height we pop it and make it the new height of a rectangle. Width goes from the new top of the stack + 1 up to current index - 1
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n+1):
            while stack and (i==len(heights) or heights[i]<=heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea