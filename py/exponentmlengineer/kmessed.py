import heapq

def heapsortbyk(array,k):
    heap = []
    returnarray = []
    size = 2*k + 1
    for i in array:
        if len(heap) == size:
            returnarray.append(heapq.heappop(heap))
        heapq.heappush(heap,i)

    while len(heap) > 0:
        returnarray.append(heapq.heappop(heap))

    return returnarray

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2

print(heapsortbyk(arr,k))
