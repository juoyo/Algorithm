import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        s.strip() 去掉首尾空格
        '''
        s = re.sub(r' +', ' ', s)
        ls = s.strip().split(' ')
        str = ''

        for i in ls[::-1]:
            if i is not ls[0]:
                str = str + i + ' '
            if i is ls[0]:
                str = str + i
        return str

s = Solution()
print(s.reverseWords("   hello   world!  "))

