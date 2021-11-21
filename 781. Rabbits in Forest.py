from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        output = 0
        for key in c.keys():
            output += math.ceil(c[key] / (key+1))* (key+1)
        return output
