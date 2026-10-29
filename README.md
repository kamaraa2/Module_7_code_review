# CST 205 Module 7: Code Review and Documentation Project

## Project Overview

This project focuses on reviewing and improving a Python program that processes numbers and strings. The goal is to make the code easier to read, understand, and maintain while keeping its original functionality.

## What the Program Does

The program has two main functions:

- `process_numbers()` takes a list of numbers, multiplies even numbers by 2, and multiplies odd numbers by 3.
- `process_strings()` checks the length of each word. Words longer than five characters are converted to uppercase, while words with five characters or fewer are converted to lowercase.

The `main()` function runs both functions and displays the results.

## Files Included

- `undocumented_script.py` — the refactored Python program.
- `CODE_REVIEW.md` — a review of the original code and the improvements made.
- `DECISIONS.md` — an explanation of the refactoring decisions.

## How to Run the Program

1. Install Python 3 if it is not already installed.
2. Open a terminal in the folder containing `undocumented_script.py`.
3. Run the following command:

   ```bash
   python undocumented_script.py
   ```

   Depending on your computer, you may need to use `python3` instead.

## Expected Output

```text
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

## Summary

The main improvements are clearer function and variable names, docstrings, and a simpler way to combine processed strings. The original number and string processing rules are preserved.