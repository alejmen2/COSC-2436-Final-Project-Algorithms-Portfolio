# Lab Report — Chapter 8: Balanced Trees

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — both tree heights, comparison counts, and the AVL result.*

```text

```=== Part 2: Watch it degenerate ===
Tree A height: 4
Tree B height: 12
Tree A in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree B in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree A search comparisons for largest value: 3
Tree B search comparisons for largest value: 12

=== Part 3: Rotate to fix it ===
AVL height after sorted insertion: 4
AVL in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]

## Reflection Questions

1. **Explain a binary search tree to someone who has never programmed.**
   When someone asks you to pick a number from 1 to 10 and whoever gets the closest wins

2. **A tree built from sorted input performs no better than a plain list. Explain why, using your own two trees.**
it doesn't split things conveniently and does things in O(n) time

3. **Chapter 8 says balanced trees are used for database indexes. Based on what you built, why is a tree a good fit for that job?**
   because the trees have fast search speeds and are also balanced so it smore organized and easier for the database to use
