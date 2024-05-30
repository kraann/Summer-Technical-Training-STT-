def reverse_string_recursive(s):
    
    if len(s) <= 1:
        return s
    
    return reverse_string_recursive(s[1:]) + s[0]


test_string = "hello"
reversed_string = reverse_string_recursive(test_string)

print(f"Original string: {test_string}")
print(f"Reversed string: {reversed_string}")
