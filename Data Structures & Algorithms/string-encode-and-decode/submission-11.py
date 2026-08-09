class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += i
            result += "µ"
        return result

       

    def decode(self, s: str) -> List[str]:
        resultsplit = []
        i = 0
        j= 0 
        while j< len(s):
            if s[j] == "µ":
                resultsplit.append(s[i:j])
                i = j + 1
            j+=1
        return resultsplit



        