from random import randrange
class RandomizedSet:

    def __init__(self):
        self.numIndex = {}
        self.arr = []
        self.numElements = 0

    def insert(self, val: int) -> bool:
        if val not in self.numIndex:
            if self.numElements == len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.numElements] = val
            self.numIndex[val] = self.numElements
            self.numElements += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.numIndex:
            return False
        ind = self.numIndex[val]
        self.arr[self.numElements-1], self.arr[ind] = self.arr[ind], self.arr[self.numElements-1]
        self.numIndex[self.arr[ind]] = ind
        self.numElements -= 1
        del self.numIndex[val]
        return True

    def getRandom(self) -> int:
        x = randrange(0, self.numElements)
        return self.arr[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
