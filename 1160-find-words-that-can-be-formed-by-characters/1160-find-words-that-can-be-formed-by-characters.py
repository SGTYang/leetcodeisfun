class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = defaultdict(int)
        for c in chars:
            char_cnt[c] += 1
        
        res = 0
        for word in words:
            word_cnt = defaultdict(int)
            for c in word:
                word_cnt[c] += 1
            good = True
            for c, freq in word_cnt.items():
                if char_cnt[c] < freq:
                    good = False
                    break
            
            if good:
                res += len(word)
        
        return res