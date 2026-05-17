class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s, key=str.lower))
        sorted_t = "".join(sorted(t, key=str.lower))
        return sorted_s == sorted_t
        