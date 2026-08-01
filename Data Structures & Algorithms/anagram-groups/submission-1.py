class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(x,y):
            if sorted(x) == sorted(y): return True
            else: return False
        output = []
        myset = set()
        c = 0
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in myset:
                for k in range(len(output)):
                    if isAnagram(strs[i] , output[k][0]):
                        output[k].append(strs[i])
            else: 
                output.append([strs[i]])
                myset.add("".join(sorted(strs[i])))
                c+=1
        return output
