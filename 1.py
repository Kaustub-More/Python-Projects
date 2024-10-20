 # Function with positional parameters
def addnumber(a, b): 
    return a + b

# Correct way to pass keyword arguments
result = addnumber(a=4, b=2)
print(result)

# Function with keyword arguments
def greet(name, age):
    print(f"Hello, {name}, your age is {age}")

# Correct way to pass keyword arguments
greet(age=30, name="Ram")