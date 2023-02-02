class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {order[i]:i for i in range(len(order))}
        
        prev = words[0]
        
        for i in range(1,len(words)):
            curr = words[i]
            flag = False
            for j in range(min(len(prev), len(curr))):
                if order_dict[prev[j]] < order_dict[curr[j]]:
                    flag = True
                    break
                elif order_dict[prev[j]] > order_dict[curr[j]]:
                    return False
                    
            if not flag and len(prev) > len(curr):
                return False
            
            prev = curr
            
        return True