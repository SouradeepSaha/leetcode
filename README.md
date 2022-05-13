# Leetcode Problem Solving Guide

## Main types of problems to solve:
- Dynamic Programming / Memoization
- Sliding Window
- Recursive / Backtracking

### Dynamic Programming Problems
The most popular types of dynamic programming problems are:
- Fibonacci Numbers:
  - Recurrence: F(n) = F(n-1) + F(n-2)
  - 1 Dimension cache using O(n) space
  - Can be solved with O(1) space in certain cases
- Zero/One Knapsack:
  - Each item can be used 0/1 times only
  - 2 Dimension cache using using O(n x m) space
- Unbounded Knapsack:
- Longest Common Subsequence
- Palindromes

### Backtracking
Run through all possible configurations of search space. Must generate each configuration exactly once. 
How to model the problem:
- Need systematic generation order to avoid repetitions
- Use vector a=(a_1, a_2, a_3,...,a_n)
- 

Applications: 
- Generate all permutations
- Generate all subsets
- Enumerate all spanning trees of graph
- All paths between two vertices
- All possible ways to partition vertices into color class
