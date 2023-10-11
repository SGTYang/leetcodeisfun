class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()

        people = [(peop, idx) for idx, peop in enumerate(people)]
        people.sort()

        ldx = 0
        curr_bloom_end = []

        res = [0]*len(people)

        for peop, idx in people:
            while ldx < len(flowers) and flowers[ldx][0] <= peop:
                if flowers[ldx][1] >= peop:
                    heapq.heappush(curr_bloom_end, flowers[ldx][1])
                ldx += 1
            
            while curr_bloom_end and curr_bloom_end[0] < peop:
                heapq.heappop(curr_bloom_end)
                
            res[idx] = len(curr_bloom_end)
        return res