class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for num, value in freq.items():
            bucket[value].append(num)
        
        res = []
        for i in range(len(bucket) -1, 0, -1):
            print(bucket[i])
            for num in bucket[i]:
                print(num)
                res.append(num)
                if len(res) == k:
                    return res
