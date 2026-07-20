class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in hash_map:
                hash_map[sort].append(s)
            else:
                hash_map[sort] = [s]
        
        return list(hash_map.values())