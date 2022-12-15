#https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = dict()
        dic2 = dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
                return False
            else:
                dic1[s[i]] = t[i]
                dic2[t[i]] = s[i]
        return True
