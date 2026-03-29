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
            if len(heap) < k:
                heapq.heappush(heap, (value, num))
            elif heap[0][0] < value:
                heapq.heappop(heap)
                heapq.heappush(heap, (value, num))
        ans = []
        for i in heap:
            ans.append(i[1])
        return ans