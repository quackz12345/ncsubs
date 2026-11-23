class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = ""
        one = True;
        while i < len(word1) and j < len(word2):
            if one:
                ans = ans + word1[i]
                i+=1
                one = False;
            else:
                ans = ans + word2[j]
                j+=1
                one = True;
        ans += word1[i:]
        ans += word2[j:]

        return ans
