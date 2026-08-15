class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicts = {}
        for i in sorted(set(nums)):
            if i in dicts:
               dicts[i] += 1 
               dicts[i+1] = dicts.pop(i)
            elif i not in dicts:
                dicts[i+1] = 1
        if nums != []: return max(dicts.values())
        else: return 0