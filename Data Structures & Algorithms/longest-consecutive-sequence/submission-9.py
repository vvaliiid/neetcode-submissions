class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsi = set(nums)
        maxi = 0
        for i in numsi:
            if i - 1 not in numsi:
                new = 1
                j= i
                while j +1 in numsi:
                    new +=1
                    j+=1
                maxi = max(new,maxi)
        return maxi