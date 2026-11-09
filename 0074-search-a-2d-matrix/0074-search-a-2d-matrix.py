class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # target value we need to search a matrix. each row is in increasing order. First integer of every row is greater than the last integer of the previous row. The way that I see it is similar to binary search where we can find the ranges. We first iterate through the columns and compare if the value is inbetween 2 rows then we know its in the previous row. if not we simply move on and compare the ranges. From there its a simple binary search or simply iterate through. It could potnetially be in the last row how do we find that? You can just binary search the matrix

        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1

        while lo<=hi:
            mid = (lo+hi)//2
            val = matrix[mid // n][mid%n]

            if val == target:
                return True
            elif val < target:
                lo = mid+1
            else:
                hi = mid - 1
        return False
            
