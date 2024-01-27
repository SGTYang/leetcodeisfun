class Solution:
    def simplifyPath(self, path):
        # . current directory
        # .. directory up a level
        # // = /
        # any other periods (...) treated as a name
        
        # /home//foo/../. - /home/
        
        # /, home, /, /(if right most elem equals to / then pop()), .
        
        path_list = path.split("/")
        stack = []
        
        for c in path_list:
            if stack and c == "..":
                stack.pop()
            elif c not in [".", "..", ""]:
                stack.append(c)
        
        return "/"+"/".join(stack)
        