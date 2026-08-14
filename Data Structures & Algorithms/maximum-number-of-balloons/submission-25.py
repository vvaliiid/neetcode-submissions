class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seti = Counter(text)
        seti['l'] = seti['l'] // 2
        seti['o'] = seti['o'] // 2


        
        return int(min(seti[k] for k in ('b','a','l','l','o','o','n') if k in seti)) 
        