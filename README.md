# SE Intern Technical Assessment — Guruvai Sciences

**Candidate:** Jessica Kumar  
**Role:** AI/ML Engineering – Agentic AI Systems  
**Platform:** Internshala  

---

## 🚀 Overview

This repository contains my solutions for the Software Engineering Internship Technical Assessment at Guruvai Sciences. The implementations focus on efficient data structures, concurrency control, and algorithmic optimization.

### Key Highlights
* **LRU Cache:** Implemented with $O(1)$ operations using a custom Hash Map and Doubly Linked List, featuring a fully thread-safe variant.
* **Event Scheduler:** Algorithmic event scheduling with overlap detection and greedy room allocation via a Min-Heap (`heapq`).

---

## 📂 Project Structure

| File | Description |
|:---|:---|
| `lru_cache.py` | Core LRU Cache implementation with built-in unit tests. |
| `thread_safe_cache.py` | Thread-safe LRU Cache extension leveraging `threading.RLock`. |
| `scheduler.py` | Interval-based Event Scheduler with collision handling and tests. |
| `assign_rooms.py` | Advanced event scheduler extension that outputs named room assignments. |

---

## 🛠️ Detailed Problem Breakdowns

### Problem 1 — LRU Cache & Thread-Safe Cache
* **Mechanism:** Combines a standard Python dictionary for $O(1)$ key lookups with a custom Doubly Linked List to maintain element recency in $O(1)$ time. 
* **Eviction Policy:** When the cache reaches its maximum capacity, the Least Recently Used (LRU) node at the tail of the list is evicted.
* **Thread Safety:** The `thread_safe_cache.py` implementation wraps critical sections using an **Reentrant Lock (`RLock`)** to safely permit concurrent `get` and `put` mutations across multiple threads without deadlocks.

### Problem 2 — Event Scheduler & Room Assignment
* **Overlap Detection:** Events are sorted chronologically by their start times to systematically evaluate schedule collisions in $O(N \log N)$ time.
* **Room Allocation:** Uses a Min-Heap to track the end times of ongoing events. This allows the system to dynamically reuse rooms as soon as they become free, minimizing total resource overhead.
* **Named Assignment:** `assign_rooms.py` builds upon this logic by mapping heap indexes to human-readable room identifiers (e.g., *Room 1*, *Room 2*), making the final schedule intuitive and actionable.

---

## 💻 How to Run & Validate

Ensure you have Python 3.x installed. You can execute the modules individually to run the code along with their integrated test suites:

```bash
# Test the core LRU Cache
python lru_cache.py

# Test the Thread-Safe LRU Cache extension
python thread_safe_cache.py

# Run the Event Scheduler and validation tests
python scheduler.py

# Run the Named Room Assignment extension
python assign_rooms.py
