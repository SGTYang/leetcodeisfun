class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()
        
        
        # slower
        word_dict = defaultdict(list)
        
        for s in strs:
            changed = "".join(sorted(s))
            word_dict[changed].append(s)
        
        return word_dict.values()
            