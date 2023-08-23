class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        price[src] = 0
        
        for i in range(k + 1):
            tmp = price.copy()
            for s, d, p in flights:
                if price[s] == float('inf'):
                    continue
                if p + price[s] < tmp[d]:
                    tmp[d] = p + price[s]
            price = tmp
        
        return -1 if price[dst] == float('inf') else price[dst]