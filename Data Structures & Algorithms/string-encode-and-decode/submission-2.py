class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "|" + word
        return encode

    def decode(self, s: str) -> List[str]:
        words = []
        num = ""
        while s != "":
            while s[0] != "|":
                num += s[0]
                s = s[1:]
            
            num = int(num)
            words.append(s[1:num+1])
            s = s[1+num:]
            num = ""
        return words
