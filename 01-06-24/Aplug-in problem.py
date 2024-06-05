str=input()

stack=[]

for i in str:
    if stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)
print("".join(stack))