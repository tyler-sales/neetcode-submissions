class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dic = {}
        t_dic = {}

        for i in range(0, len(s)):
            s_dic[s[i]] = 1 + s_dic.get(s[i], 0)
            t_dic[t[i]] = 1 + t_dic.get(t[i], 0)
        
        return s_dic == t_dic