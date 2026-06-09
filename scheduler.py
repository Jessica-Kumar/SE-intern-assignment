import heapq

def can_attend_all(events):
    events.sort(key=lambda x: x[0])
    for i in range(1, len(events)):
        if events[i][0] < events[i-1][1]:
            return False
    return True

def min_rooms_required(events):
    if not events:
        return 0
    events.sort(key=lambda x: x[0])
    heap = []
    for start, end in events:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


# ─── TEST ─────────────────────────────────
print("=" * 40)
print("EVENT SCHEDULER")
print("=" * 40)

e1 = [(9,10),(10,11),(11,12)]
print("events :", e1)
print("can_attend_all     →", can_attend_all(e1))
print("min_rooms_required →", min_rooms_required(e1))

print()
e2 = [(9,11),(10,12),(11,13)]
print("events :", e2)
print("can_attend_all     →", can_attend_all(e2))
print("min_rooms_required →", min_rooms_required(e2))

print()
e3 = [(8,12),(9,11),(10,14),(11,13)]
print("events :", e3)
print("can_attend_all     →", can_attend_all(e3))
print("min_rooms_required →", min_rooms_required(e3))
