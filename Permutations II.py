class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(counts, arr):
            #print(counts)
            empty = True
            for key, val in counts.items():
                if val != 0:
                    counts[key] -= 1
                    arr.append(key)
                    backtrack(counts, arr)
                    counts[key] += 1
                    arr.pop()
                    empty = False
            
            if empty:
                result.append([x for x in arr])
        
        backtrack(Counter(nums), [])
        return result
