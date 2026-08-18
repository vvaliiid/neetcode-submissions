class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        s_result = set()
        

        for i in range(len(nums)):
            for j in self.twoSu(nums[:i] + nums[i+1:], -nums[i]):
                complement = j
                if complement != []:
                   complement = complement + [nums[i]]
                   tupl = (complement[0],complement[1],complement[2])
                
                   if sorted(tupl) not in result:
                      result.append(sorted(complement))

        return result
    def twoSu(self, lista, target):

        s = Counter(lista)
        result = []

        for x in set(lista):
            el = target - x
            if el in s: 
                if (el == x and s[el] >=2) or el != x:    
                   result.append([x, el])
        return result