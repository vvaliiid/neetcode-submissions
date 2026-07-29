class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        MySet = set()
        for i in range(len(nums)):
            if nums[i] in MySet:
                return True
            else: 
                MySet.add(nums[i])
        return False
        