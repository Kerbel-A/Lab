#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            l = tuple(sorted(str))
            if l not in res.keys():
                res[tuple(l)] = [str]
            else:
                res[tuple(l)].append(str)
        
        return res.values() 
