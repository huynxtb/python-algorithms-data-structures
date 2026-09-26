import heapq
import math
import random
from typing import Any, Callable, Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar("T")


def _get_rng(rng: Optional[random.Random]) -> random.Random:
    """Helper to return an existing Random instance or the global random module."""
    return rng if rng is not None else random._inst  # type: ignore[attr-defined]


def reservoir_sample(iterable: Iterable[T], k: int, rng: Optional[random.Random] = None) -> List[T]:
    """
    Select a uniform random sample of k items from an iterable using Alan G. Waterman's Algorithm R.

    Mathematical Guarantee:
        For a stream of length n, every subset of size k has equal probability of being chosen,
        and each item in the stream has an exact probability of min(1.0, k / n) of being in the
        final sample.

    Complexity:
        - Time Complexity: O(n) calls to uniform random number generation.
        - Space Complexity: O(k) auxiliary memory to hold the reservoir.

    Args:
        iterable: An input stream or collection of items of arbitrary/unknown length.
        k: The desired sample size. Must be non-negative.
        rng: Optional instance of random.Random for deterministic execution.

    Returns:
        A list containing up to k uniformly sampled items from the iterable.

    Raises:
        ValueError: If k is negative.
    """
    if k < 0:
        raise ValueError(f"Sample size k must be non-negative, got {k}")
    if k == 0:
        return []

    r = _get_rng(rng)
    iterator = iter(iterable)
    reservoir: List[T] = []

    for item in iterator:
        reservoir.append(item)
        if len(reservoir) == k:
            break

    if len(reservoir) < k:
        return reservoir

    count = k
    for item in iterator:
        count += 1
        # Generate a random integer in [0, count - 1]
        idx = r.randint(0, count - 1)
        if idx < k:
            reservoir[idx] = item

    return reservoir


class ReservoirSampler(Generic[T]):
    """
    A stateful reservoir sampler implementing Algorithm R for unbounded streaming data.

    Maintains a uniform random sample of at most k items seen across arbitrary sequences
    of .add() invocations.
    """

    def __init__(self, k: int, seed: Optional[Any] = None) -> None:
        """
        Initialize the ReservoirSampler.

        Args:
            k: Maximum capacity of the sample reservoir. Must be non-negative.
            seed: Optional seed value to initialize internal PRNG.

        Raises:
            ValueError: If k is negative.
        """
        if k < 0:
            raise ValueError(f"Sample size k must be non-negative, got {k}")
        self._k: int = k
        self._rng: random.Random = random.Random(seed)
        self._reservoir: List[T] = []
        self._total_seen: int = 0

    @property
    def capacity(self) -> int:
        """Return the maximum capacity k of the reservoir."""
        return self._k

    @property
    def total_seen(self) -> int:
        """Return the total number of items observed in the stream so far."""
        return self._total_seen

    def add(self, item: T) -> bool:
        """
        Process a single item from the stream and update the reservoir.

        Args:
            item: The element to ingest.

        Returns:
            True if the item was placed into the reservoir, False otherwise.
        """
        if self._k == 0:
            self._total_seen += 1
            return False

        self._total_seen += 1
        if len(self._reservoir) < self._k:
            self._reservoir.append(item)
            return True

        idx = self._rng.randint(0, self._total_seen - 1)
        if idx < self._k:
            self._reservoir[idx] = item
            return True

        return False

    def get_sample(self) -> List[T]:
        """
        Return a shallow copy of the current sample reservoir.

        Returns:
            A list of elements currently held in the reservoir.
        """
        return list(self._reservoir)

    def clear(self) -> None:
        """Reset the reservoir sampler state."""
        self._reservoir.clear()
        self._total_seen = 0


def reservoir_sample_fast(stream: Iterable[T], k: int, rng: Optional[random.Random] = None) -> List[T]:
    """
    Select a uniform random sample of k items using Kim-Hung Li's Algorithm L.

    Instead of generating random numbers for every item in the stream, Algorithm L
    computes geometric jump lengths (S) to determine how many items to discard before
    the next reservoir replacement occurs. This drastically reduces PRNG calls from O(n)
    to O(k * (1 + log(n / k))).

    Mathematical Guarantee:
        Produces an identical uniform distribution to Algorithm R while skipping items in O(1)
        expected step calculation per accepted item.

    Complexity:
        - Time Complexity: O(k + k * log(n / k)) expected random generation calls and arithmetic operations.
        - Space Complexity: O(k) auxiliary memory.

    Args:
        stream: An input stream or collection of items of arbitrary/unknown length.
        k: The desired sample size. Must be non-negative.
        rng: Optional instance of random.Random for deterministic execution.

    Returns:
        A list containing up to k uniformly sampled items from the stream.

    Raises:
        ValueError: If k is negative.
    """
    if k < 0:
        raise ValueError(f"Sample size k must be non-negative, got {k}")
    if k == 0:
        return []

    r = _get_rng(rng)
    iterator: Iterator[T] = iter(stream)
    reservoir: List[T] = []

    for item in iterator:
        reservoir.append(item)
        if len(reservoir) == k:
            break

    if len(reservoir) < k:
        return reservoir

    # W is an exponential transform tracking the threshold probability parameter
    # In Algorithm L: W = exp(log(U) / k) where U ~ Uniform(0, 1)
    u = r.random()
    while u == 0.0:
        u = r.random()
    w = math.exp(math.log(u) / k)

    while True:
        # S is the geometric jump: number of items to skip
        u_s = r.random()
        while u_s == 0.0:
            u_s = r.random()
        
        log_w = math.log(w)
        if log_w == 0.0:
            s = 0
        else:
            s = math.floor(math.log(u_s) / math.log(1.0 - w))

        # Skip S items in the iterator
        skipped = 0
        selected_item: Optional[T] = None
        exhausted = False

        for _ in range(s + 1):
            try:
                selected_item = next(iterator)
                skipped += 1
            except StopIteration:
                exhausted = True
                break

        if exhausted or skipped <= s or selected_item is None:
            break

        # Replace a random item in the reservoir with the selected item
        replace_idx = r.randint(0, k - 1)
        reservoir[replace_idx] = selected_item

        # Update W parameter
        u_w = r.random()
        while u_w == 0.0:
            u_w = r.random()
        w *= math.exp(math.log(u_w) / k)

    return reservoir


def weighted_reservoir_sample(
    iterable: Iterable[T],
    k: int,
    weight_func: Callable[[T], float],
    rng: Optional[random.Random] = None,
) -> List[T]:
    """
    Select a weighted random sample of k items without replacement using Algorithm A-Res
    (Pavlos S. Efraimidis and Paul G. Spirakis).

    Each item i is assigned a key k_i = u_i^(1 / w_i), where u_i ~ Uniform(0, 1) and w_i > 0
    is the weight of item i. The k items with the largest keys are returned.

    Complexity:
        - Time Complexity: O(n log k) using a min-heap of size k.
        - Space Complexity: O(k) auxiliary memory for the priority queue.

    Args:
        iterable: An input stream or collection of items.
        k: The desired sample size. Must be non-negative.
        weight_func: A callable mapping each item to a positive numeric weight (w > 0).
        rng: Optional instance of random.Random for deterministic execution.

    Returns:
        A list containing up to k items sampled proportionally to their weights without replacement.

    Raises:
        ValueError: If k is negative or if any item has a non-positive weight.
    """
    if k < 0:
        raise ValueError(f"Sample size k must be non-negative, got {k}")
    if k == 0:
        return []

    r = _get_rng(rng)
    # Min-heap storing tuples of (key, insertion_counter, item)
    # insertion_counter ensures stable tie-breaking and comparison safety
    heap: List[tuple[float, int, T]] = []
    counter = 0

    for item in iterable:
        weight = float(weight_func(item))
        if weight <= 0.0 or math.isnan(weight):
            raise ValueError(f"Item weight must be strictly positive and finite, got {weight}")

        u = r.random()
        while u == 0.0:
            u = r.random()

        # Key r = u^(1/w)
        key = math.pow(u, 1.0 / weight)
        counter += 1

        if len(heap) < k:
            heapq.heappush(heap, (key, counter, item))
        else:
            if key > heap[0][0]:
                heapq.heapreplace(heap, (key, counter, item))

    return [item for _, _, item in heap]
