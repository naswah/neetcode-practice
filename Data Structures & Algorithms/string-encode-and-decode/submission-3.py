class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str= ""
        for i in strs:
                final_str += str(len(i))+ '#' + i
        return final_str

    def decode(self, s: str) -> List[str]:
        res= []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            res.append(word)
            i = j+1+length
        return res
