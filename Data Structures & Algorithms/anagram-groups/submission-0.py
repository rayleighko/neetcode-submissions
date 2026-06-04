class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # day 1 - use hashmap - watch solution
        # Time complexity: O(m∗n)
        # Space complexity:
        #   - O(m) auxiliary space, excluding the returned output.
        #   - O(m∗n) total space if the output groups are counted.
        res = defaultdict(list) # mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
        # day 1 - anouther solution - just sortting
        # Time complexity: O(m∗nlogn)
        # Space complexity: O(m∗n)
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())