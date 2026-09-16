class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        pq = []
        for n in counter.keys():
            heapq.heappush(pq, (-counter[n], n))

        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])

        return res