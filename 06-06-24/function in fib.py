def fin(n):
  if n<=0:
    print("invalid input")
  elif n < len(fibVal):
    return fibVal[n]
  fibVal.append(fibVal(n-1)+fibVal(n-1))
  return fibVal[n]

fibVal = [0,1]

print(fin(int(input())))