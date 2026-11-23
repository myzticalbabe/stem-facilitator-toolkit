# Lesson Plan: Functions and Parameters

## Objectives
- Students will define functions with def
- Students will use parameters and return values
- Students will distinguish local vs global scope
- Students will write reusable functions with docstrings

## Materials
- Computer with Python 3
- Projector
- Handout: "Function Anatomy" diagram
- Peer review checklist

## Steps

### 1. Warm-Up (5 min)
Show two code snippets that do the same calculation.
Ask: "Which is easier to reuse? Why?"

### 2. Direct Instruction (15 min)
- Define: `def greet(name): return f"Hello, {name}!"`
- Call: `greet("Alice")`
- Parameters vs arguments
- return vs print
- Default parameters: `def greet(name="friend"):`
- Scope: local variables inside functions

### 3. Guided Practice (15 min)
Students write:
```python
def area_rectangle(width, height):
    """Return area of a rectangle."""
    return width * height

def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0

# Test
print(area_rectangle(5, 3))  # 15
print(is_even(4))  # True
```

### 4. Independent Practice (10 min)
Students write a function `grade_score(score)` that returns "A/B/C/D/F" based on score ranges. Include docstring.

### 5. Exit Ticket (5 min)
1. What keyword defines a function? (def)
2. What does `return` do? (sends value back to caller)
3. Write a function `double(x)` that returns x*2.

## Assessment
- Exit ticket: 3 questions
- Code review: function naming, docstrings, correct return
- Extension: recursive factorial function
