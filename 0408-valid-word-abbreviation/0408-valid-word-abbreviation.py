class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pointer = 0
        abbr_pointer = 0
        curr = ""
        
        while abbr_pointer < len(abbr):
            if abbr[abbr_pointer].isdigit():
                if curr == "" and abbr[abbr_pointer] == "0":
                    return False
                curr += abbr[abbr_pointer]
            else:
                if curr != "":
                    word_pointer += int(curr)
                
                if word_pointer >= len(word) or word[word_pointer] != abbr[abbr_pointer]:
                    return False
                
                word_pointer += 1
                curr = ""
            abbr_pointer += 1
        
        if curr != "":
            word_pointer += int(curr)
        
        return word_pointer == len(word) and abbr_pointer == len(abbr)
                