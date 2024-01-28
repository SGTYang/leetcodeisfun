class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # "abc", "ace" - > diff group
        # create dict, k: (diff) v: list
        diff = defaultdict(list)
        
        # O(n*c)
        # O(n)
        for string in strings:
            if len(string) == 1:
                diff[(-1)].append(string)
            else:
                tmp = []
                prev = string[0]
                for i in range(1, len(string)):
                    res = ord(prev) - ord(string[i])
                    if res < 0:
                        res += 26
                    tmp.append(res)
                    prev = string[i]
                diff[tuple(tmp)].append(string)
        
        return list(diff.values())