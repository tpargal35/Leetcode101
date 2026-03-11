# ─────────────────────────────────────────────
# APPROACH 1: HashSet
# ─────────────────────────────────────────────
# Idea: keep a set of "seen" numbers.
# If a number is already in the set → it's the duplicate.
# Time:  O(n)  — one pass through the array
# Space: O(n)  — set grows up to n elements
# ─────────────────────────────────────────────
def findDuplicate_set(nums: List[int]) -> int:
    seen = set()                # empty set to track visited numbers
    for num in nums:
        if num in seen:         # already visited → duplicate found
            return num
        seen.add(num)           # mark as visited


# ─────────────────────────────────────────────
# APPROACH 2: HashMap (Dictionary)
# ─────────────────────────────────────────────
# Idea: use a dict to count how many times each number appears.
# The moment a count hits 2 → that's our duplicate.
#
# Why use a dict instead of a set here?
#   - A set only stores existence (True/False).
#   - A dict stores a KEY → VALUE pair, so you can track counts,
#     indices, or any extra info per number.
#   - For THIS problem a set is simpler, but dict is useful when
#     you need frequency info (e.g. "which number appears 3 times?")
#
# Time:  O(n)  — one pass through the array
# Space: O(n)  — dict grows up to n entries
# ─────────────────────────────────────────────
def findDuplicate_map(nums: List[int]) -> int:
    count = {}                          # key: number, value: how many times seen
    for num in nums:
        count[num] = count.get(num, 0) + 1  # increment count (default 0 if not seen)
        if count[num] == 2:             # seen twice → duplicate!
            return num



# ─────────────────────────────────────────────
# APPROACH 3: Floyd's Cycle Detection (Tortoise & Hare)
# ─────────────────────────────────────────────
# Key insight:
#   Treat each value in the array as a "next pointer",
#   just like a linked list node → nums[i] points to nums[nums[i]].
#
#   Example: nums = [1, 3, 4, 2, 2]
#   index:           0  1  2  3  4
#   0 → nums[0]=1 → nums[1]=3 → nums[3]=2 → nums[2]=4 → nums[4]=2 → nums[2]=4 ...
#                                                              ↑ CYCLE starts at 2 ↑
#
#   Because two indices point to the same value (the duplicate),
#   following the "pointers" will always create a cycle.
#   The ENTRY POINT of that cycle = the duplicate number.
#
# Phase 1 — Find intersection point inside the cycle:
#   slow moves 1 step at a time, fast moves 2 steps.
#   They MUST meet inside the cycle eventually.
#
# Phase 2 — Find the cycle entry (= duplicate):
#   Reset one pointer to start (index 0).
#   Move both one step at a time → they meet at the duplicate.
#
# Time:  O(n)  — linear
# Space: O(1)  — only two pointers, no extra data structure! ✅
# ─────────────────────────────────────────────
def findDuplicate_floyd(nums: List[int]) -> int:
    # Phase 1: detect cycle
    slow = nums[0]          # tortoise: 1 step
    fast = nums[nums[0]]    # hare: 2 steps

    while slow != fast:
        slow = nums[slow]           # move 1 step
        fast = nums[nums[fast]]     # move 2 steps

    # Phase 2: find cycle entry = duplicate
    slow = 0                # reset slow to the start
    while slow != fast:
        slow = nums[slow]   # both move 1 step now
        fast = nums[fast]

    return slow             # meeting point = duplicate


# ── Test ──────────────────────────────────────
nums = [1, 3, 4, 2, 2]
print("Set approach :", findDuplicate_set(nums))   # 2
print("Map approach :", findDuplicate_map(nums))   # 2
print("Floyd approach:", findDuplicate_floyd(nums)) # 2

