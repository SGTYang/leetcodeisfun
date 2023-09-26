class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        word_dict = {}
        stack = []
        visited = set()
        for i in range(len(s)):
            word_dict[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and word_dict[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        
        return "".join(stack)