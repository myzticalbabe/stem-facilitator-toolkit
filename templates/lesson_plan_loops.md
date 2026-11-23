# Lesson Plan: Loops and Iteration

## Objectives
- Students will write for-loops to iterate over sequences
- Students will write while-loops with proper termination
- Students will use range() with start, stop, step
- Students will identify and fix infinite loops

## Materials
- Computer with Python 3
- Projector
- Handout: "Loop Patterns" reference card
- Timer for activity

## Steps

### 1. Warm-Up (5 min)
Show a repetitive task: printing "Hello" 10 times.
Ask: "How can we avoid writing print 10 times?"

### 2. Direct Instruction (15 min)
- for-loop over a list: `for item in ["a", "b", "c"]: print(item)`
- range(): `for i in range(5):`, `range(2, 10, 2)`
- while-loop: `count = 0; while count < 5: ...; count += 1`
- Infinite loop warning: missing increment
- break and continue keywords

### 3. Guided Practice (15 min)
Students complete:
```python
# Print even numbers 0-20
for i in range(0, 21, 2):
    print(i)

# Sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)
```

### 4. Independent Practice (10 min)
Students write a program that asks the user for a number N and prints the multiplication table for N (1-10).

### 5. Exit Ticket (5 min)
1. What does `range(3, 8)` produce? (3,4,5,6,7)
2. When does a while-loop stop? (When condition is False)
3. Fix: `i = 0; while i < 5: print(i)` (missing i += 1)

## Assessment
- Exit ticket: 3 questions
- Code review: correct loop syntax and termination
- Challenge: nested loop to print a 5x5 grid
