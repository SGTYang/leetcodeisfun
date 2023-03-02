class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        point1 = 0
        point2 = 1
        # chars = ["a","b","b"]

        if len(chars)==1:
            return len(chars)
        for i in range(1,len(chars)):

            # print(chars[i])
            if chars[point1] == chars[i]:
                # print(chars[i])
                # print(i,chars[i])
                point2 += 1
                # print(point2)
                if(i==len(chars)-1):
                    s+=chars[len(chars)-1]+str(point2)
                    
            elif chars[point1]!= chars[i]:
                if(point2!=1):
                    s += chars[point1] + str(point2)
                else:
                    s+=chars[point1]
                
                point1 = i
                point2 = 1
                
                if(i==len(chars)-1):
                    if(point2!=1):
                        s+=chars[len(chars)-1]+str(point2)
                    else:
                        s+=chars[len(chars)-1]
                        
                    
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)
        # print(s)