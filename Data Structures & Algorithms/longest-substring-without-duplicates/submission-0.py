class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = {}
        max_size = 0
        length = 0

        for index, char in enumerate(s):
            if char not in seen:
                seen[char] = index
            else:
                l = max(l, seen[char] + 1)
                seen[char] = index

            length = (index - l) + 1
            max_size = max(max_size, length)

        return max_size