class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_grp = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in ana_grp:
                ana_grp[key] = []

            ana_grp[key].append(s)

        
        return list(ana_grp.values())