class TimeMap:
    # so the same key can have multiple values at different timestamps. So the key for example alice can have another set inside of it that is keyed by time where we should be able to search for that value based on time and if it doesnt exist we get the nearest timestamp. So if key = alice and value = happy time = 1 we can then have sad and time = 2 and we should be able to get it for both 1 and 2. So realistically what this structure looks like is a nested set. Therefore it should be a key as its base. And then for each key it has a set. that is then keyed by the timestamp and then it has a value. 

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not in we simply make it an empty array otherwise we are appending to the existing array
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # now because the array by property will always be sorted we can binary search on this. So we are looking for the mood at whatever timestamp but a mood can just not change after a certain period so we could be sad at 3 but then not change till like 5 so if i search for 4 i need to find the value that is less than or equal to 4 but also the greatest value that was previously added into the array. 
        res, values = "", self.keyStore.get(key, []) # this get isnt recursive its just getting the values associated with the key.
        l, r = 0, len(values) - 1 # so values looks like [[happy, 1],[sad, 2]] etc. 

        while l<=r:
            m = (l+r)//2

            if values[m][1] <= timestamp: # this is a valid potential valus so we change. Eventually ending where res is the right most value 
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)