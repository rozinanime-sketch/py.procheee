pdd = ["A", "A", "M", "M", "T"]

def bSort(arr = pdd, index = {"A": 3, "M": 2, "T": 3},):
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if index[arr[j]] < index[arr[j + 1]]:

    return arr
print(bSort(pdd))


