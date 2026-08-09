class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + ","+  i
        return str(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i < len(s):
            tul = ""
            while s[i].isdigit():
               tul += s[i]
               i+=1
               if s[i] == ","  : break

            decode.append(s[i+1:i+(int(tul))+1])
            i += int(tul) +1
        return decode