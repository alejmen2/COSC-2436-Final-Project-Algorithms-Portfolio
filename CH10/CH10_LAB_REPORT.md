# Lab Report — Chapter 10: Greedy Algorithms

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your scheduling result, both knapsack answers side by side, your set cover, and your subset counts.*

```text

```Scheduled classes
[('Art', 9.0, 10.0), ('Math', 10.0, 11.0), ('Music', 11.0, 12.0)]

Part 2: Brute-force knapsack choice
[('laptop', 2000, 3), ('guitar', 1500, 1)]

Part 2: Brute-force knapsack value
3500
Part 2: Gap between brute force and greedy
500

Part 3: Stations chosen by greedy set cover
['kone', 'ktwo', 'kthree', 'kfive']
Part 3: Number of subsets an exact solver checks for n=5
32
Part 3: Number of subsets an exact solver checks for n=20
1048576
Part 3: Number of subsets an exact solver checks for n=100
1267650600228229401496703205376
## Reflection Questions

1. **Explain the greedy strategy to someone who has never programmed.**
   scheduling your classes when you new semester has started

2. **Greedy was perfect for scheduling and wrong for the knapsack. What changed about the problem?**
   knapsack is is undividable where scheduling can be dividable and overlapped
   

3. **You already wrote a greedy algorithm in an earlier lab — building the Huffman tree in Chapter 7 repeatedly merges the two lowest-frequency nodes. Is that one exactly optimal, or an approximation?**
   it is exactly optimal, it exact code for a given set of frequencies 
