class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        boom = 1
        for i in nums:
                
            boom *= i
        result = [boom for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] != 0:
               result[i] = int(result[i] / nums[i])
            elif nums[i] == 0:
                boom = 1 
                for j in range(len(nums)):
                    if j != i:
                       boom*=nums[j]
                result[i] = boom
        return result
        