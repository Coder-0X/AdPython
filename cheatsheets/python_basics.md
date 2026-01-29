# 🐍 Python Basics Cheatsheet

## Variables & Data Types
```python
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True # Boolean
items = [1, 2]  # List
info = {"a": 1} # Dictionary
```

## String Operations
```python
s = "Hello World"
print(s.lower())       # "hello world"
print(s[0:5])          # "Hello"
print(f"Msg: {s}")     # f-string formatting
```

## Lists
```python
nums = [1, 2, 3]
nums.append(4)         # Add to end
nums.pop()             # Remove last
print(len(nums))       # Length
```

## Dictionaries
```python
user = {"name": "Bob", "age": 30}
print(user["name"])    # Access
user["city"] = "NY"    # Add/Update
del user["age"]        # Remove
```

## Loops
```python
# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    count += 1
```

## Functions
```python
def greet(name):
    return f"Hi, {name}!"

result = greet("Alice")
```
