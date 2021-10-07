class Solution:
    def backtrack(self, left, right, cur, output):
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            output.append(cur)
            return
        if left == right: 
            self.backtrack(left-1, right, cur + "(", output)
        else:
            self.backtrack(left-1, right, cur + "(", output)
            self.backtrack(left, right-1, cur + ")", output)
        
    
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.backtrack(n, n, "", output)
        return output
