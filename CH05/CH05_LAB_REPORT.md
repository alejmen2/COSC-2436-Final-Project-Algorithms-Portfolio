# Lab Report — Chapter 5: Hash Tables

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your cache hit/miss output and your collision comparison.*

```text

```MISS: /home
Contents of /home
MISS: /about
Contents of /about
HIT: /home
Contents of /home
MISS: /contact
Contents of /contact
HIT: /about
Contents of /about
HIT: /home
Contents of /home
apple -> 1
banana -> 2
Load factor: 0.6
Bad hash -> collisions: 5 longest chain: 5
Simple hash -> collisions: 4 longest chain: 4

## Reflection Questions

1. **Explain a hash table to someone who has never programmed.**
   a hash table is like lockers that have names for each one

2. **Chapter 5 says lookups are fast "on average." When is that not true, and what makes it go wrong?**
  lookups go from O(1) to O(n) whenever there is a lot of collisions

3. **Your page cache avoided repeating expensive work. Where have you seen caching in software you use?**
  when looking up things on the internet, it remembers what you looked up so it becomes faster overtime.
