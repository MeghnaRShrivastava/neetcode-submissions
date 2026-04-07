class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        hashmap = {}
        for j in range(len(s)):
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)
            ans = max(ans, j-i+1)
            hashmap[s[j]] = j+1
        return ans

    


