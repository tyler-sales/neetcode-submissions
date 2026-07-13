class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in hm:
                hm[sort_word] = [word]
            else:
                hm.get(sort_word).append(word)
                
        
        groups = []
        for ana in hm.values():
            groups.append(ana)
        return groups