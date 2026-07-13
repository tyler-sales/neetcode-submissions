class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        words_s, words_t = {}, {}
        for i in range(len(s)):
            words_s[s[i]] = 1 + words_s.get(s[i], 0)
            words_t[t[i]] = 1 + words_t.get(t[i], 0)
        
        return words_s == words_t
    

            


        #ss = sorted(s)
        #ts = sorted(t)
        #return ss == ts