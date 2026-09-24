class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array of numbers and we are given an integer k. return the k most frequent elements within the array. What does that actually mean? This means if im given k=1 then we return the single most frequent number. if we are given k=2 then we return the 2 most frequent items. So what is my initial intuition? I can take a hash count the occurence of each number and then have the set ordered from greatest to least and then simply add the key of the first k elements. Now this in terms of time complexity would be around so this would be n around O(nlogn)

        countedValues = defaultdict(int)
        kElements = []
        for num in nums:
            countedValues[num] += 1
        sortedValues = sorted(countedValues.items(), key=lambda x: x[1], reverse=True)

        for x in range(k):
            kElements.append(sortedValues[x][0])

        return kElements