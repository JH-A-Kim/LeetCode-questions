class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ## number of rows is numRows the number of rows is also the number of values in that row. Each value is the sum of the 2 values above it. Each edge value is always one. But how does that look like in an array. What is the smallest subproblem i can find. To find the value its always the sum of the previous arrays values at the same index and previous index I have to start off with generating an 2 x 2 array. 
        pascalsTriangle=[]
        row=0
        while row<numRows:
            arrayRow=[]
            col=0
            while col < row+1:
                if col == 0 or col==row:
                    arrayRow.append(1)
                else:
                    arrayRow.append(pascalsTriangle[row-1][col]+pascalsTriangle[row-1][col-1])
                col+=1
            pascalsTriangle.append(arrayRow)
            row+=1

        return pascalsTriangle
                
        