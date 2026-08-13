from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seti = Counter(text)
        c = 0
        for i in range(len(text)):
            if (seti['b']>=1) and (seti['a']>=1) and (seti['l']>=2) and (seti['o']>=2) and (seti['o']>=1) and (seti['n'] >=1) :
                c+=1
                seti['b']-=1
                seti['a']-=1
                seti['l']-=1
                seti['l']-=1
                seti['o']-=2
                seti['n']-=1
        return c
        