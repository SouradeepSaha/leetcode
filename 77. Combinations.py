class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def recurse(ind, cur):
            if ind > n:
                return
            if len(cur) == k:
                output.append([x for x in cur])
            else:
                cur.append(ind+1)
                recurse(ind+1, cur)
                cur.pop()
                recurse(ind+1, cur)
            
        
        recurse(0, [])
        return output
