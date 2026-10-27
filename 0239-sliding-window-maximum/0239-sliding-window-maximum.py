class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We are given an array of integers and a integer k. There exists a sliding window of k. Starts at left of the array and slides one position to the right until it reaches the right edge. Return a list that contains the max element in the window at each step. So realistically we could keep track of the the values coming in and out. Create a set that contains each value and we take the max at each step. And then simply append it to a output list. This would end up being O(n x n ) Can we not just use a max heap? the array is simply a max heap and we simply remove the character that is no longer in the window. And simply use whatever is still the max at each iteration.
        heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap[0][1] <= i-k: # this is just seeing if the current max is outside the window if so we simply pop it because we are keeping track of both the max and its index and then we simply keep going until the max is inside the window otherwise the heap is self updating. 
                    heapq.heappop(heap)
                output.append(-heap[0][0])

        return output


