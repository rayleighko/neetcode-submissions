class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # arr = []

        # for num, cnt in count.items():
        #     arr.append([cnt, num])

        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])

        # return res

        # day 1 - watch solution
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res