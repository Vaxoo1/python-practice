Absolutely. I'll turn everything we've learned so far into **clean reference notes**—concepts and rules only, without the hands-on projects or diagrams.

# Python — Data Manipulation Notes

## 1. Lists

A **list** stores multiple values in a single variable.

```python
prices = [100, 105, 102, 110]
```

Lists are:

* Ordered
* Mutable
* Zero-indexed
* Able to contain duplicate values

Access an element:

```python
prices[0]
```

Result:

```text
100
```

---

## 2. Indexing

Python list indexes start at `0`.

```text
Value:   100   105   102   110
Index:     0     1     2     3
```

Important:

```python
prices[index]
prices[index + 1]
```

`index + 1` accesses the next element.

---

## 3. `len()`

`len()` tells you how many elements are in a list.

```python
len(prices)
```

If there are 4 elements:

```text
len(prices) → 4
```

The final valid index is:

```text
len(prices) - 1
```

---

## 4. Consecutive List Comparison

When analyzing changes between neighboring values:

```python
for index in range(len(prices) - 1):
```

We compare:

```python
prices[index]
prices[index + 1]
```

Why `-1`?

Because the final element has no next element.

---

# 5. Difference / Change

For sequential data:

```python
change = next_value - current_value
```

This produces a **signed change**.

Example:

```text
100 → 105 = +5
105 → 102 = -3
```

The sign tells you the direction.

---

## 6. Increase Detection

An increase occurs when:

```python
next_value > current_value
```

The amount of increase is:

```python
change = next_value - current_value
```

Example:

```text
100 → 105
105 > 100
change = 5
```

---

## 7. Decrease Detection

A decrease occurs when:

```python
current_value > next_value
```

The decrease amount should be positive:

```python
change = current_value - next_value
```

Example:

```text
110 → 95
110 > 95
change = 15
```

### Important

Don't accidentally do:

```python
change = next_value - current_value
```

for a decrease, because that gives:

```text
95 - 110 = -15
```

when we usually want the **decrease magnitude**:

```text
15
```

---

# 8. Unchanged Values

When:

```python
current_value == next_value
```

there is no increase or decrease.

The movement is:

```text
0
```

---

# 9. Signed Change vs Movement Magnitude

This distinction is extremely important.

### Signed change

```python
change = next_value - current_value
```

Preserves direction.

```text
100 → 105 = +5
105 → 102 = -3
```

### Movement magnitude

Magnitude means **how far the value moved**, regardless of direction.

```text
100 → 105 = 5
105 → 102 = 3
110 → 95 = 15
```

For now, you've learned to calculate this manually:

```python
if current_value > next_value:
    movement = current_value - next_value
else:
    movement = next_value - current_value
```

This is essentially manually implementing the idea behind:

```python
abs(next_value - current_value)
```

but we intentionally haven't used `abs()` yet.

---

# 10. Counters

A counter keeps track of how many times something happens.

Initialize:

```python
count = 0
```

When the event occurs:

```python
count += 1
```

Example concept:

```text
increase happens → count increases by 1
```

---

# 11. Running Total

A running total accumulates values as the loop processes them.

Initialize:

```python
total = 0
```

Then:

```python
total += change
```

Example:

```text
change = 5
total = 5

change = 3
total = 8

change = 7
total = 15
```

---

# 12. Running Maximum

A running maximum finds the largest value **without using `max()`**.

Initialize:

```python
largest = None
```

Then:

```python
if largest is None or current_value > largest:
    largest = current_value
```

The important idea:

> Keep the best value found so far.

Every new value gets compared against the current best.

---

# 13. Why Initialize With `None`

`None` represents:

> **No meaningful value has been found yet.**

Example:

```python
largest = None
```

When the first valid value arrives:

```python
if largest is None or value > largest:
    largest = value
```

This is safer than using:

```python
largest = 0
```

because `0` might be a legitimate result.

---

# 14. `None` vs Truthiness

Do **not** use:

```python
if largest:
```

to mean:

> "Does a largest value exist?"

Because `0` is falsy.

Instead:

```python
if largest is not None:
```

This specifically asks whether a value has been established.

---

# 15. Boolean Flags

A Boolean flag tracks whether an event has happened.

Example:

```python
increase_found = False
```

When the first increase occurs:

```python
increase_found = True
```

Then:

```python
if not increase_found:
```

means:

> The event has not happened yet.

---

# 16. Boolean Flag vs Numeric Value

These answer different questions.

```python
increase_found
```

answers:

> Did an increase happen?

Whereas:

```python
largest_increase
```

answers:

> What was the largest increase?

Don't use one variable to represent both concepts.

---

# 17. First Occurrence Tracking

To capture the **first time** something happens:

```python
if not increase_found:
    # capture information
    increase_found = True
```

The flag prevents later occurrences from replacing the first one.

Typical information captured can include:

```python
starting_price
ending_price
starting_index
ending_index
```

---

# 18. `break` vs Boolean Flags

### `break`

Stops the loop completely.

```python
break
```

Use it when you genuinely want:

> Stop processing now.

### Boolean flag

Allows the loop to continue while remembering that something happened.

```python
found = True
```

Use it when you need to:

> Continue processing the rest of the data but remember an earlier event.

These are not interchangeable.

---

# 19. Percentage Change

Percentage change is:

```python
change / starting_value * 100
```

For example:

```text
100 → 110

change = 10

10 / 100 × 100 = 10%
```

The starting value is important because it is the baseline.

---

# 20. Undefined Percentage

If the starting value is `0`, percentage change cannot be calculated normally because division by zero is invalid.

Instead of crashing:

```python
if starting_value == 0:
    percentage_change = None
else:
    percentage_change = change / starting_value * 100
```

This follows an important pattern:

> If a calculation has no meaningful value, use `None` and allow the program to continue.

---

# 21. Comparing Percentage Values

If a percentage may be `None`, don't compare it directly.

First establish that it has a value:

```python
if percentage_change is not None:
```

Then perform the comparison.

This prevents invalid comparisons involving `None`.

---

# 22. Python `or` and Short-Circuiting

This pattern:

```python
if largest is None or value > largest:
```

works because Python evaluates `or` from left to right.

If:

```python
largest is None
```

is `True`, Python doesn't need to evaluate the second condition.

This allows the first valid value to initialize the running maximum.

---

# 23. Variable Initialization

Variables that will be used later should be initialized appropriately before the loop when necessary.

For example:

```python
largest = None
found = False
total = 0
count = 0
```

Choose the initial value based on the **meaning of the variable**, not simply because Python requires a value.

---

# 24. Scope / Conditional Initialization

Be careful when creating a variable inside a condition:

```python
if condition:
    result = something

print(result)
```

Ask:

> Can every path reaching `print(result)` guarantee that `result` was created?

If the answer is no, you can get an error.

This is especially important when storing information about the first occurrence of an event.

---

# 25. Running State

**Running state** means information that the program continuously maintains while processing data.

Examples:

```python
count
total
largest
first_occurrence
found
```

The loop updates the state as it processes each element.

This is one of the most important patterns we've learned so far.

---

# 26. Related State

Sometimes one result requires several pieces of information.

For example, finding the largest movement isn't enough. You may also need:

```text
largest movement
starting value
ending value
starting index
ending index
direction
```

These pieces describe **the same event**.

Important rule:

> When a new best result is found, update all information belonging to that result together.

Otherwise you can accidentally produce mismatched data—for example, the largest movement from one pair but the prices from another pair.

---

# 27. Snapshot Concept

When you find a new largest result:

```python
if movement > largest_movement:
```

you don't just save the number.

You capture a **snapshot of the event**:

```python
largest_movement = movement
starting_price = current_price
ending_price = next_price
starting_index = index
ending_index = index + 1
```

This connects the calculated result to the original data that produced it.


# 28. State Tracking, Direction + Magnitude
## What is state tracking?

State tracking means maintaining information about what the program has discovered so far while processing data.

A loop can continuously update this information as it examines each value.

Examples of state:

* count
* total
* largest value
* smallest value
* whether something has been found
* first occurrence
* information belonging to the current best result

---

## Running State

A running state is information that changes as the loop processes each element.

Example:

```python
count = 0
total = 0
largest = None
```

The loop updates these variables as it processes the data.

---

## Running Maximum

A running maximum keeps track of the largest value found so far.

```python
largest = None

if largest is None or value > largest:
    largest = value
```

The important idea is:

> Compare the current value with the best value found so far.

If the current value is better, replace the previous best.

---

## Tracking Related State

Sometimes finding the largest value is not enough.

For example, if we find the largest price movement, we may also need to know:

```text
largest movement
starting price
ending price
starting index
ending index
direction
```

These values all describe the same event.

When a new largest result is found, all related information must be updated together.

Example:

```python
if movement > largest_movement:
    largest_movement = movement
    starting_price = current_price
    ending_price = next_price
    starting_index = index
    ending_index = index + 1
```

This creates a snapshot of the event that produced the current best result.

---

## Snapshot Concept

A snapshot means capturing all relevant information about a result at the moment it becomes the best result.

For example:

```text
movement = 25
starting price = 95
ending price = 120
starting index = 5
ending index = 6
direction = increase
```

These values belong together because they describe the same movement.

---

## Important Rule

> When a new best result is found, update every piece of information that belongs to that result at the same time.

Otherwise, the program can accidentally combine information from different events.

For example:

```text
largest movement → from index 5 → 6
starting price   → from index 2
```

That would produce an incorrect result.

---

## Direction + Magnitude

When analyzing movement, direction and magnitude are separate concepts.

### Direction

Signed change tells us the direction:

```python
change = next_value - current_value
```

Example:

```text
100 → 105 = +5  → Increase
105 → 102 = -3  → Decrease
```

### Magnitude

Magnitude tells us how far the value moved without caring about direction.

```text
100 → 105 = 5
105 → 102 = 3
110 → 95  = 15
```

Therefore, a movement can have:

```text
Magnitude: 15
Direction: Decrease
```

Both pieces of information can be tracked together.

---

## Why State Tracking Matters

State tracking is a fundamental programming pattern.

It allows a program to process data one element at a time while remembering important information from everything it has already processed.

This pattern is used for:

* finding maximum/minimum values
* counting events
* calculating totals
* finding first occurrences
* tracking best/worst results
* analyzing sequences
* searching for patterns
* many algorithm and DSA problems

---

## Current Learning Position

Python

→ Data Manipulation

→ Sequential Data Analysis

→ Running State

→ State Tracking

→ Tracking Related Information

This is the current topic we are practicing.
