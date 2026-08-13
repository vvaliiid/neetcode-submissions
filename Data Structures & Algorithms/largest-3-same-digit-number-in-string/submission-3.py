class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = []
       
        for left in range(len(num)-2):
            if int(num[left]) == int(num[left+1]) == int(num[left+2]):
                res  = num[left] + num[left] + num[left+2]
                result.append(int(res))
            left+=1
        if result:
           if max(result) == 0:
               return "000"
           return str(max(result))
        else: return ""