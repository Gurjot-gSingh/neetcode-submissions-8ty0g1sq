import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for i in nums:
            print(i)
            if i in frequency:
                print(i)
                frequency[i] += 1
            else:
                frequency[i] = 1
        heap = []
        print(frequency)
        for num, value in frequency.items():
            print(num, value)
            if len(heap) < k:
                print(i)
                heapq.heappush(heap, (value, num))
            elif heap[0][0] < value:
                heapq.heappop(heap)
                heapq.heappush(heap, (value, num))
        ans = []
        for i in heap:
            ans.append(i[1])
        return ans