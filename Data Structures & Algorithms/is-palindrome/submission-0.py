class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        a = set("azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890")
        ss = ""
        for k in s:
            if k in a:
                ss = ss + k
        
        n = len(ss)
        left = 0
        right = n-1

        while left <=right:
                if ss[left] != ss[right] : 
                    return False
                left += 1
                right -= 1
        
        return True