class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if (strs is None) or (len(strs) == 0):
            return prefix
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if len(word) == i or word[i] != char:
                    return prefix
            prefix += char
        return prefix

        
        

