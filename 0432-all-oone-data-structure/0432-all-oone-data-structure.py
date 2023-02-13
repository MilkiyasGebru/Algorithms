class AllOne:

    def __init__(self):
        self.values = defaultdict(set)
        self.keys = defaultdict(int)
        self.maxx = 0
    def inc(self, key: str) -> None:
        
        self.keys[key] += 1
        self.values[self.keys[key]].add(key)
        self.maxx = max( self.maxx, self.keys[key])
    def dec(self, key: str) -> None:
        self.values[self.keys[key]].remove(key)
        if len(self.values[self.maxx]) == 0:
            self.maxx -= 1
        self.keys[key] -= 1
        if self.keys[key] == 0:
            del self.keys[key]

    def getMaxKey(self) -> str:
        if not self.keys:
            return ""
        for x in self.values[self.maxx]:
            return x
        # return max(self.keys,key=self.keys.get)

    def getMinKey(self) -> str:
        if not self.keys:
            return ""
        return min(self.keys,key=self.keys.get)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()