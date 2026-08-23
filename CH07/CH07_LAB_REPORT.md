# Lab Report — Chapter 7: Trees and Huffman Coding

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your BFS and DFS orders, your encode/decode round trip, and your bit counts.*

```text

```=== Part 2: DFS vs BFS Shortest Path ===
DFS found target: target (took the FAR path)
BFS found target: target (took the CLOSE path)

Frequencies: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Codes: {'a': '0', 'c': '100', 'd': '101', 'r': '110', 'b': '111'}
Encoded bitstring: 01111100100010101111100
Decoded text: abracadabra
Huffman bits: 23  vs  fixed-width bits: 88

## Reflection Questions

1. **Explain the difference between BFS and DFS to someone who has never programmed.**
   looking from folder to folder, vs. looking in a folder and into all the files then looking at the other folder

2. **Why do frequent letters get shorter codes? Use your own code table.**
   frequent letters get shorter codes because they come up more often in the system so to lessen the bytes the words take it is lowered

3. **Your decoder reads a stream of bits with no separators and still gets it right. Why is there never any ambiguity?**
   because no words ends at the start of another word
