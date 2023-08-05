class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for i in range(len(strs)):
            anagram = [0] * 26
            for c in strs[i]:
                anagram[ord(c) - ord("a")] += 1
            res[tuple(anagram)].append(strs[i])
        
        return res.values()