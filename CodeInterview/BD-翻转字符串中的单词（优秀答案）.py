class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = s[::-1]
        answer = ' '.join(s)
        return answer

s = Solution()
print(s.reverseWords("   hello   world!  "))
