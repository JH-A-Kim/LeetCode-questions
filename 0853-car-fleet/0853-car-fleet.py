class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car fleet n cars traveling down a one lane highway. 2 arrays of integers position and speed. Both of length n. Positions of the ith car in miles and the speed of the ith car in mph. destination is at target miles. Car can NOT pass another car ahead of it and can only catch up to another car and then drive at the same speed. Car fleet is a non empty set of cars driving at the same position and same speed. A single car is also a car fleet. return the number of different car fleets that will arive at the destination. first find greatest position, everything is gated behind that. and its speed. then we update its position at each hour. everything else has to match that. So its kept out of the stack we could take the speed of the greatest position see how fast it takes for it to get to the end. And then calculate the length of time that is greater and sort the array positions such that lowest position to greatest position. and then backwards iterate where every value if 0,1,4,7 (0 takes 10)(1 takes 5)(4 takes 3)(7 takes 3)
# if anything before 7 is faster or the same speed thats one group and we can ignore the grouped values and then we pop all those values off the stack as one group and iterate the counter by one. we then take the next largest value in the stack compare it to the next and then see if they are grouped and then pop all the grouped values continuing until completed. That should give us the total number of groups. TLDR we get arrival times anything that arrives faster than our current group leader is part of the group that gets popped. anything slower does not get popped and becomes a new group leader. Arrival time i didnt understand but everything else i came up with

        arrival_times = []
        zip(position, speed)
        sortedCars = sorted(zip(position, speed))

        count = 0

        for i in range(len(sortedCars)):
            arrival_times.append((target - sortedCars[i][0])/sortedCars[i][1])
        
        

        # calculate on the stack anything equal to or faster we pop together.
        while arrival_times:
            group_leader = arrival_times[-1]

            while arrival_times and arrival_times[-1] <= group_leader:
                arrival_times.pop()

            count+=1
        
        return count