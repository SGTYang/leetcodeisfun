class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand_cnt = Counter(hand)
        
        min_heap = list(hand_cnt.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in hand_cnt:
                    return False
                hand_cnt[i] -= 1
                if hand_cnt[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True