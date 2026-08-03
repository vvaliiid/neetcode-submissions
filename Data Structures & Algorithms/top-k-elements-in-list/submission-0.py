class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        result = []
        for i in nums:
            if i in dicts:
                dicts[i]+=1
            else:
                dicts[i] = 0
        while k>0:
            maxi = max(dicts, key = dicts.get)
            result.append(maxi)
            k-=1
            dicts.pop(maxi)
        
        return result
        