class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        for s in strs:
            cnt = {}
            for c in s:
                if c in cnt:
                    cnt[c]+=1
                else:
                    cnt[c]=1
            key = tuple(sorted(cnt.items()))
            if key in grouping:
                grouping[key].append(s)
            else:
                grouping[key]= [s]

        return list(grouping.values())
