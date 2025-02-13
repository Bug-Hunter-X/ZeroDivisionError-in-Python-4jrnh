def my_function(a, b):
    if b == 0:
        return 0  # Or raise an exception, or handle it differently
    return a / b

result = my_function(10, 0)
print(result) # Output: 0
result2 = my_function(10,2)
print(result2) # Output: 5.0