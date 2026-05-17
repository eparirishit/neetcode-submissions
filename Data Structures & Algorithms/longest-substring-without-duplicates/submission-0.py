class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            res = max(res, len(char_set))
            char_set = set()
        return res