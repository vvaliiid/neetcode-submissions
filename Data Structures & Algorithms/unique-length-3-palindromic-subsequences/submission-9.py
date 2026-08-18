class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        for c in set(s):                    
            i, j = s.find(c), s.rfind(c)    
            if j - i < 2:                   
                continue
            result += len(set(s[i + 1:j]))  
        return result