# Reservoir Sampling Family (Algorithm R, Algorithm L, and Algorithm A-Res)

## 1. Introduction

Reservoir sampling is a family of randomized algorithms designed to select a representative, random sample of $k$ items from a sequence, stream, or dataset of unknown, dynamic, or potentially infinite length in a single sequential pass. It is particularly useful when:
- The total number of items $n$ is unknown ahead of time.
- The dataset cannot fit entirely into main memory.
- Data arrives continuously in a real-time streaming pipeline.

This implementation includes:
1. **Algorithm R (Waterman / Knuth)**: The classic streaming uniform sampling algorithm.
2. **Stateful `ReservoirSampler`**: A class-based encapsulation of Algorithm R suited for continuous event listeners.
3. **Algorithm L (Kim-Hung Li)**: An optimized algorithm that uses geometric skip-distances to skip generating random numbers for items that will not enter the reservoir, dramatically improving processing speed.
4. **Algorithm A-Res (Efraimidis & Spirakis)**: A weighted reservoir sampling algorithm without replacement based on exponential key generation.

---

## 2. Usage


import random
from reservoir_sampling import (
    reservoir_sample,
    ReservoirSampler,
    reservoir_sample_fast,
    weighted_reservoir_sample,
)

# 1. Functional Uniform Reservoir Sampling (Algorithm R)
stream = range(1, 1000001)
sample_r = reservoir_sample(stream, k=5, rng=random.Random(42))
print("Algorithm R sample:", sample_r)

# 2. Stateful Streaming Reservoir Sampler
sampler = ReservoirSampler(k=3, seed=42)
for item in ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]:
    sampler.add(item)
print("Streamed Sample:", sampler.get_sample())
print("Total items seen:", sampler.total_seen)

# 3. High-Performance Jump-based Reservoir Sampling (Algorithm L)
large_stream = (x for x in range(10_000_000))
sample_l = reservoir_sample_fast(large_stream, k=5, rng=random.Random(42))
print("Algorithm L sample:", sample_l)

# 4. Weighted Reservoir Sampling (Algorithm A-Res)
weighted_items = [
    {"name": "low_priority", "weight": 1.0},
    {"name": "medium_priority", "weight": 10.0},
    {"name": "high_priority", "weight": 100.0},
    {"name": "critical_priority", "weight": 1000.0},
]

sample_weighted = weighted_reservoir_sample(
    weighted_items,
    k=2,
    weight_func=lambda x: x["weight"],
    rng=random.Random(42),
)
print("Weighted sample:", [item["name"] for item in sample_weighted])


---

## 3. Detailed Explanation

### Algorithm R
Maintains a buffer (the "reservoir") of size $k$. The first $k$ elements are placed directly into the reservoir. For each subsequent element at 1-based index $i > k$, a random integer $j \in [0, i - 1]$ is generated. If $j < k$, the item at `reservoir[j]` is replaced with the new element. By mathematical induction, the probability of any item remaining in the reservoir after $n$ elements is exactly $\min(1, k/n)$.

### Algorithm L
Algorithm R spends $O(n)$ random generation calls even though the probability of replacement drops to $k/i$ as $i$ grows large. Algorithm L computes the number of non-sampled items $S$ to skip before the next replacement occurs using the geometric distribution parameter $W = \exp(\ln(U)/k)$. It skips $S = \lfloor \ln(U') / \ln(1 - W) \rfloor$ items in a single step, reducing the number of PRNG calls to $O(k \log(n/k))$.

### Algorithm A-Res (Weighted Sampling)
To sample items proportional to non-uniform weights $w_i > 0$ without replacement, Algorithm A-Res generates a key $r_i = u_i^{1 / w_i}$ for each item, where $u_i \sim \text{Uniform}(0, 1)$. The algorithm maintains a min-heap of size $k$ tracking the $k$ items with the largest keys.

---

## 4. Complexity Analysis

| Algorithm | Operation | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Algorithm R** (`reservoir_sample`) | Ingest $n$ items | $O(n)$ | $O(k)$ |
| **ReservoirSampler** | Single `add(item)` | $O(1)$ | $O(k)$ |
| **Algorithm L** (`reservoir_sample_fast`) | Ingest $n$ items | $O(k + k \log(n/k))$ expected PRNG calls, $O(n)$ item traversals | $O(k)$ |
| **Algorithm A-Res** (`weighted_reservoir_sample`) | Ingest $n$ items | $O(n \log k)$ | $O(k)$ |