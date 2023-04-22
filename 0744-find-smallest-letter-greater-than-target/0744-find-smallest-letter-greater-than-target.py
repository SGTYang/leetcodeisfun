class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target or letters[0] > target:
            return letters[0]
        
        l,r = 0, len(letters)-1
        while l <= r:
            mid = (l+r)//2
            
            if letters[mid] > target:
                r = mid - 1
            if letters[mid] <= target:
                l = mid + 1
        
        return letters[l]