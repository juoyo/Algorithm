"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        slen = len(s)
        if slen < 4 or slen > 12:
            return
        for i in range(0, 4):  # 1<= i <=3
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    s1 = s[0:i + 1]
                    s2 = s[i + 1:j + 1]
                    s3 = s[j + 1:k + 1]
                    s4 = s[k + 1:slen]
                    if self.isValid(s1) and self.isValid(s2) and self.isValid(s3) and self.isValid(s4):
                        ip=s1+'.'+s2+'.'+s3+'.'+s4
                        res.append(ip)
        return res

    def isValid(self, str):
        if len(str) > 3 or len(str) < 1 or int(str) > 255 or (str[0] == '0' and len(str) > 1):
            return False
        else:
            return True


s = Solution()
print(s.restoreIpAddresses("25525511135"))


