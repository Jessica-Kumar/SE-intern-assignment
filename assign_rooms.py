import heapq
from typing import List, Tuple

def assign_rooms(events):
    sorted_events = sorted(enumerate(events), key=lambda x: x[1][0])
    heap = []
    names = []
    result = [None] * len(events)
    for orig_idx, (start, end) in sorted_events:
        if heap and heap[0][0] <= start:
            _, room = heapq.heapreplace(heap, (end, heap[0][1]))
        else:
            room = f'Room-{chr(ord("A") + len(names))}'
            names.append(room)
            heapq.heappush(heap, (end, room))
        result[orig_idx] = (room, start, end)
    return result

events = [(9, 10), (9, 11), (10, 12)]
for room, s, e in assign_rooms(events):
    print(f'{room}: {s}:00 - {e}:00')