# Lab Report — Chapter 3: Recursion

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output, including part of the call-stack trace.*

```Result: /root/docs/notes.txt
   Result: None
   Total files: 3
   Total size: 370
   === Tree view ===
root
  readme.txt
  docs
    notes.txt
    archive
      old.txt
  empty_folder
Traceback (most recent call last):
  File "/home/user/main.py", line 162, in <module>
    print_tree_with_depth(fs)

```

## Reflection Questions

1. **Explain recursion to someone who has never programmed.**
   Its opening boxes that contain more boxes in them and the cycle repeats
2. **An empty folder is a legitimate base case, not an error. Why does treating it as an error break the program?**
   it triggers false alarms that make the recursion stop
3. **A folder nested 10,000 levels deep would crash your code. Why?**
   because of stack overflow, it would be too big for recursion's memory limit
