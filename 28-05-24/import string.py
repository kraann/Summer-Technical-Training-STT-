import string
strnum=input()
for i in strnum:
    if i not in string.digits:
        print("false")
        break
else:
    print("true")