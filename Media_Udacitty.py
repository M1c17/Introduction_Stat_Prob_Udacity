data1 = [1, 4, 5, 10, -20, 1]
data2 = [1, 4, 5, 10, -20]

def median(data):
    sdata = sorted(data)
    index = (len(data) - 1) // 2
    print(index)
    return sdata[index]

print(median(data1))
print(median(data2))