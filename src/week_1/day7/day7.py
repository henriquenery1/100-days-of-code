def mergeArrays(targetArray, sourceArray):

  for x in range(0, len(sourceArray)):
    for y in range(0, len(targetArray)):
      if sourceArray[x] <= targetArray[y]:
        targetArray.insert(targetArray.index(targetArray[y]),sourceArray[x])
        break
      elif sourceArray[x] >= targetArray[y] and y == len(targetArray)-1:
        targetArray.append(sourceArray[x])
        break
  return targetArray