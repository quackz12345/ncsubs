class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        chars = {}
        ans = 0

        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1

            while (right - left + 1) - max(chars.values()) > k:
                chars[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans