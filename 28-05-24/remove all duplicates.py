def remove_duplicates(input_string):
    if not input_string: 
        return input_string
    
    result = input_string[0]  
    
    
    for char in input_string[1:]:
        
        if char != result[-1]:
            result += char
    
    return result


input_string = input("Enter a string: ")


print("Original string:", input_string)
print("String after removing consecutive duplicates:", remove_duplicates(input_string))
