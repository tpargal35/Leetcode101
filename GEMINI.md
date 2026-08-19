# LeetCode Step-by-Step Pair Programming Mode

## Allowed Category Folders
Only use these existing workspace categories (do not create new top-level categories):
- `Advanced Graphs`
- `Arrays & Hashing`
- `Backtracking`
- `Binary Search`
- `Bit Manipulation`
- `Dynamic Programming`
- `Graphs`
- `Greedy`
- `Intervals`
- `Linked List`
- `Math & Geometry`
- `Sliding Window`
- `Stack`
- `Strings`
- `Trees`
- `Tries`
- `Two Pointers`

## Problem Setup Workflow
- **Auto-Setup on Problem Prompt**: Whenever the user provides a LeetCode problem number or name:
  1. Map it to one of the **existing category folders** listed above.
  2. Create `<Category Folder>/<number>-<problem-name>.py`.
  3. Include standard imports (`List`, `Optional`, `Dict`, etc.).
  4. Use a **standalone top-level function signature** (NO `class Solution`, NO `self` parameter).
  5. Include `pass` inside the function body as a placeholder.
  6. Automatically add the official LeetCode example test cases with variable definitions and a `print(...)` call.
  7. Wait for the user's first step without writing any solution logic.

### Example Setup File Output
If the user prompts: `"Leetcode 1386 Cinema Seat Allocation"`:
The agent creates `Arrays & Hashing/1386-cinema-seat-allocation.py` with:
```python
from collections import defaultdict
from typing import List

def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
    pass

# Example 1
n = 3
reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
print(maxNumberOfFamilies(n, reservedSeats))
```

## Core Directives
- **Incremental Implementation ONLY**: Implement ONLY what the user explicitly asks for in each prompt. Do NOT jump ahead, write full solutions, or complete future algorithm steps prematurely unless specifically instructed.
- **Preserve User Code & Test Cases**: Never overwrite or discard user-defined test cases, variables, or functions. Always retain existing context and append or edit surgically.
- **Comment Non-Optimal Solutions for Reference**: If an intermediate or non-optimal solution is built or being replaced by a more optimal one, keep the previous solution commented out with a clear label (e.g. `# Approach 1: <Name> / Non-Optimal`) so it remains for reference, and allow the user to build the optimal solution step-by-step.
- **Concise & Direct Responses**: Keep answers short, showing only the changes made and asking for the next instruction.
- **Collaborative Flow**: Let the user drive the problem-solving strategy, data structure choices, and logic step-by-step.
