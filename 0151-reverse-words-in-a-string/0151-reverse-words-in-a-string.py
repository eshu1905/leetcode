class Solution:
    def reverseWords(self, s: str) -> str:
        worde=s.split()
        worde.reverse()
        reverse=" ".join(worde)
        return reverse      