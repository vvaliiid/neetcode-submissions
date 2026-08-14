class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seti = Counter(text)
        if seti['l'] %2 == 0:
            seti['l'] = (seti['l']/2)
        elif  seti['l'] %2 == 1:
             seti['l']  = (seti['l'] - 1)/2

        if seti['o'] %2 == 0:
            seti['o'] = (seti['o'] / 2)
        elif  seti['o'] %2 == 1:
             seti['o']  = (seti['o'] - 1)/2
        
        return int(min(seti[k] for k in ('b','a','l','l','o','o','n') if k in seti)) 