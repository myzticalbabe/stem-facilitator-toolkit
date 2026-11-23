# Lesson Plan: Variables and Data Types in Python

## Objectives
- Students will define and use variables in Python
- Students will identify int, float, str, and bool data types
- Students will convert between data types using int(), float(), str()
- Students will write a short program using variables

## Materials
- Computer with Python 3 installed
- Projector for live coding
- Handout: "Variable Cheat Sheet" (attached)
- Whiteboard and markers

## Steps

### 1. Warm-Up (5 min)
Ask: "What is a variable in math? (e.g., x in x + 3 = 7)"
Connect to programming: a variable is a named container for data.

### 2. Direct Instruction (15 min)
- Demonstrate creating variables: `name = "Alice"`, `age = 14`, `gpa = 3.8`, `is_student = True`
- Show `type()` function to inspect data types
- Explain type conversion: `int("5")`, `float(3)`, `str(42)`
- Common errors: `int("hello")` raises ValueError

### 3. Guided Practice (15 min)
Students write in pairs:
```python
first_name = "Jordan"
birth_year = 2010
current_year = 2026
age = current_year - birth_year
print(f"{first_name} is {age} years old")
```

### 4. Independent Practice (10 min)
Students create variables for their own info and print a formatted bio.

### 5. Exit Ticket (5 min)
1. What type is `3.14`? (float)
2. What does `str(100)` return? ("100")
3. Write one line creating a boolean variable.

## Assessment
- Exit ticket: 3 questions, 2/3 to pass
- Code review: variable naming conventions (snake_case)
- Participation in pair activity
