numList = list(map(int,input().split()))
for ele in range(len(numList)):
  if numList[ele] % 2 == 0:
    if numList[ele] != int(numList[ele]):
      print("False")
      break
    else:
      if '.' in str(numList[ele]):
        print("False")
        break
      else:
        print("False")