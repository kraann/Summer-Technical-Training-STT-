s = input("Enter a string: ")

stack = []

for char in s:
    stack.append(char)

reversed_s = ''

while stack:
    reversed_s += stack.pop()

if s == reversed_s:
    print(f"It is a palindrome.")
else:
    print(f"It is not a palindrome.")
