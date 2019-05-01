class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        ls = []
        for i in path:
            if i:
                ls.append(i)
        stack = []
        for i in ls:
            if i == '.' or i == ' ':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        urlpath = '/' + '/'.join(stack)
        return urlpath
s = Solution()
print(s.simplifyPath("/a//b////c/d//././/.."))