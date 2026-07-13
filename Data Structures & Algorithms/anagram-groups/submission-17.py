class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        final = []
        
        for word in strs:
            order = "".join(sorted(word))
            if anagrams.get(order) != None:
                anagrams.get(order).append(word)
            else:
                anagrams[order] = [word]
        return list(anagrams.values())
        
        for words in anagrams.values():
            final.append(words)
        return final
            