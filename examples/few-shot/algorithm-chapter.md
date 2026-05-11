# Few-Shot: Algorithm Chapter

## Problem Framing

Given an array and a limit on the number of modifications, the task is to maximize the length of a segment that can be made valid. The input size is large enough that enumerating every segment and rebuilding its state would be too slow.

## Baseline And Bottleneck

The direct baseline is to test each interval independently. Even if validity can be checked in linear time per left endpoint, the total cost is quadratic. The bottleneck is that adjacent intervals share almost all of their information, but the baseline discards it.

## Core Observation

For a fixed right endpoint, if an interval is valid, then removing elements from the left cannot make it invalid. This monotonicity lets us maintain the minimal left boundary with a sliding window.

## Algorithm Design

We scan the right endpoint from left to right. The maintained state records the current interval and the number of modifications needed to make it valid. Whenever the cost exceeds the limit, we move the left endpoint until validity is restored. The best answer is the maximum window length seen after restoration.

## Correctness

The algorithm never misses an optimal interval because every right endpoint is considered. For that endpoint, the while loop stops at the smallest left boundary that makes the interval valid; every longer invalid interval has already been excluded, and every shorter valid interval is no better than the maintained one.

## Complexity

Each endpoint moves monotonically from left to right. Therefore the time complexity is `O(n)`, and the space complexity is `O(1)` or `O(|Σ|)` depending on the maintained frequency structure.

## Edge Cases

The implementation must handle empty windows after shrinking, limits equal to zero, and repeated values that make the maintained cost change by more than one if updated in the wrong order.
