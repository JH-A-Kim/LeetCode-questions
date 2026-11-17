class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the median in 2 integer arrays of size m and n. Where both are srted in ascending order. needs to run O(log(n+m)). So what defines the median it should be either the middle value. Or the 2 middle values added and then divided by 2. theoretically I can merge the 2 arrays using a merge function that automatically sorts as we iterate through the array and then just use the indexes to find the middle point or middle points. but this would be a O(n) or O(m) solution. Not meeting the run time requirement. Theoretically I can 
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B)<len(A):
            A,B = B,A
        
        l, r = 0, len(A)-1

        while True:
            i = (l+r) // 2
            j = half - i -2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j+1)<len(B) else float("infinity")

            if Aleft <= Bright and Bleft <=Aright:
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright, Bright)) / 2
            elif Aleft>Bright:
                r = i - 1
            else:
                l = i + 1

