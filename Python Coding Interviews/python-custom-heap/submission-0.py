import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    h = []
    for num in nums:
        pair = (abs(num), num)
        heapq.heappush(h, pair)
    new_h = []
    while h:
        pair = heapq.heappop(h)
        o_num = pair[1]
        new_h.append(o_num)
    new_h.sort()
    return o_num


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
