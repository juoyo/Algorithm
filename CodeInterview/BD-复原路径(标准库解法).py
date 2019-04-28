import os.path
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        urlpath = os.path.abspath(path)
        return urlpath

s = Solution()
print(s.simplifyPath("/a//b////c/d//././/.."))










