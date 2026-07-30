class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] +=1
            else:
                dic[s[i]] = 1
        for j in range(len(t)):
            if t[j] in dic:
                dic[t[j]] -= 1 
            else: return False
        for k in range(len(s)):
            if dic[s[k]] != 0:
                return False
        return True
            