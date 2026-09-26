class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


# Example
s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s, t))