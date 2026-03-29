import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        heap = []
        for num, value in frequency.items():
            heapq.heappush(heap, (value, num))
            if len(heap) >k:
                heapq.heappop(heap)
        ans = []
        for i in heap:
            ans.append(i[1])
        return ans