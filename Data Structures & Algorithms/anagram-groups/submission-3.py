class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        output = []
        myset = set()
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in myset:
                for k in range(len(output)):
                    if sorted(strs[i]) == sorted(output[k][0]):
                        output[k].append(strs[i])
            else: 
                output.append([strs[i]])
                myset.add("".join(sorted(strs[i])))

        return output
