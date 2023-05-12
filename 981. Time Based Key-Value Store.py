class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        low, high = 0, len(self.timemap[key])-1
        ans = (-1, "")
        while low <= high:
            mid = (low+high)//2
            #print(self.timemap[key])
            if self.timemap[key][mid][0] == timestamp:
                return self.timemap[key][mid][1]
            elif self.timemap[key][mid][0] > timestamp:
                high = mid-1
            else:
                low = mid+1
                ans = ans if ans[0] >  self.timemap[key][mid][0] else self.timemap[key][mid]
        #print(ans)
        return ans[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
