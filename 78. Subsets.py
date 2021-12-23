class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def recurse(index, cur):
            if index >= len(nums):
                output.append([x for x in cur])
            else:
                cur.append(nums[index])
                recurse(index+1, cur)
                cur.pop()
                recurse(index+1, cur)
        
        recurse(0, [])
        return output
        
