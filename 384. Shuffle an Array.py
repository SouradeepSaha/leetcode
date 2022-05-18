import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        newArr = [_ for _ in self.arr]
        boundary = 0
        while boundary < len(newArr):
            index = random.randint(boundary, len(newArr)-1)
            newArr[index], newArr[boundary] = newArr[boundary], newArr[index]
            boundary += 1
        
        return newArr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
