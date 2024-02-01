def getDifferentNumber(array):
    n = len(array)
    total = n*(n+1)/2
    sumarray = 0
    for num in array:
        sumarray += num
    return int(total - sumarray)

print(getDifferentNumber([0,2,1,3,5]))
