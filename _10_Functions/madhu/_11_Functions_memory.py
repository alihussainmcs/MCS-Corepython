
x = 10
print("x details : ", x, id(x))


# Function memory allocation

def get_data():   # Function invocation
    print("Welcome to my method")
    return "Hello World"

res = get_data()   # Function calling
print("Result is : ", res)

print("Function details ", get_data)  # Get function body address


# Mutable,Immutable :: Pass by value ,Pass by reference
# Copy : Shallow copy,Deep copy

