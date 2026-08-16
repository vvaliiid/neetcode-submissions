class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = -1001
        for i in range(len(numbers)):

            a = numbers[i]
            if a == prev:
                continue
            else:
                prev = a
            missing = target - a

            idx = self.binary_search(numbers[i+1:], missing)
            # print(idx, numbers[i+1:], missing)
            if idx != -1:
                return [i+1, idx+i+1]

        return []

    def binary_search(self, lx, target):

        left = 0
        right = len(lx)-1
        m = 10
        while left <= right:
            m -= 1
            middle = (left + right) // 2
            # print(left, right, middle, lx)

            check = lx[middle]
            if check == target:
                return middle+1
            
            if check > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1


    
        