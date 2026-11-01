class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Given an array of integers temperatures, where temperatures[i] is the temp on that given day. return an array result where result i is the oh so I have a temperature and i need to see how many days until we reach a hotter day. Realistically I can use indexes from the end index - first index. A rudimentary solution would be something like i take the ith value and iterate from there until a greater value appears if not set to 0 and then move on to the next value. This would be O(n^2) so not the most efficient. Where could I take this to not constantly repeat work. If i take a window where i keep track of each value with the max heap. Doesnt need to be max never mind. If i use an ordered stack so a monotonic stack I can keep it in tuples where i have the value and its index. So what it looks like is that whenevere we add a value to the stack we first check if its greater then the top if it is we pop and we continue until we are not greater at which we append to the stack. And we calculate the difference in indices to count the distance and then we continue until the end which gives us O(n) time O(n) space. 
        res = [0] * len(temperatures)
        stack = [] # and this needs to be tuples of the temp and index

        for i in range(len(temperatures)):
            if stack == []:
                stack.append((temperatures[i], i))
            while stack and temperatures[i]>stack[-1][0]:
                    values = stack.pop()
                    res[values[1]] = i - values[1]
            stack.append((temperatures[i], i))
                

        return res