class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                lcp += a[0]
            else:
                return lcp
        return lcp