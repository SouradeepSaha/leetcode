# 17. Letter Combinations of a Phone Number
from typing import List

class Solution:

    def letterCombHelper(self, digits: str, word: str, ind: int):
        if ind >= len(digits):
            self.arr.append(word)
            return
        for letter in self.keypad[int(digits[ind])]:
            self.letterCombHelper(digits, word + letter, ind+1)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.arr = []
        self.keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.letterCombHelper(digits, "", 0)
        return self.arr
    
