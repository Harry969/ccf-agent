# Few-Shot: Algorithm Chapter

## Problem Framing

Given an input sequence, a budget, and a validity condition, the task is to find the best feasible solution under the budget. The input size is large enough that a direct search over all candidates is not practical.

## Baseline And Bottleneck

The direct baseline tests each candidate independently. Even when each test is linear, the total cost becomes quadratic or worse. The bottleneck is that adjacent candidates share most of their state, but the baseline discards that reuse.

## Core Observation

For a fixed right boundary, feasibility is monotone in the left boundary. Once an interval becomes valid, shrinking it from the left cannot break validity. This monotonicity gives a one-way update rule.

## Algorithm Design

We scan the right boundary from left to right. The maintained state tracks the current interval, the resource usage inside it, and the best feasible answer seen so far. Whenever the resource limit is exceeded, we move the left boundary until feasibility is restored. The best answer is the maximum valid state encountered after restoration.

## Correctness

The algorithm never misses an optimal interval because every right boundary is considered. For that boundary, the restoration loop stops at the smallest left boundary that makes the interval feasible. Any longer invalid interval has already been excluded, and any shorter valid interval is no better than the maintained one.

## Complexity

Each boundary moves monotonically from left to right. Therefore the time complexity is `O(n)`, and the space complexity is `O(1)` or `O(|\Sigma|)` depending on the maintained summary structure.

## Edge Cases

The implementation must handle empty windows after shrinking, budgets equal to zero, and repeated values that change the maintained cost by more than one if the updates are applied in the wrong order.
