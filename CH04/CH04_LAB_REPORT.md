# Lab Report — Chapter 4: Quicksort

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your benchmark table — all six rows, including any `RecursionError`.*

```text

```Part 3: Benchmark
shape             strategy    result            
------------------------------------------------
unsorted          first       0.001594 s        
unsorted          random      0.001816 s        
sorted            first       RecursionError    
sorted            random      0.001684 s        
reverse sorted    first       RecursionError    
reverse sorted    random      0.001564 s   

## Reflection Questions

1. **Explain quicksort to someone who has never programmed.**
   Splitting a number table in half between numbers that are greater or lesser than the number chosen
2. **A random pivot usually avoids the worst case. Why does randomness help here?**
   because it avoids being chosen at the beginning which is the worst case because then it runs O(n) time
3. **Where does sorting show up in software you actually use?**
   Dictionaries, you look through the dictionary to find words and you look for them alphabetically, in which they have to be sorted to do that.
