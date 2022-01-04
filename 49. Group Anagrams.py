from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            
            words[s].append(word)
        
        return words.values()
        
