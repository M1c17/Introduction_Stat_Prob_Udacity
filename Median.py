data1 = [1, 2, 5, 10, -20, 1]
data2 = [1, 2, 5, 10, -20]

def median(data):
    # Insert your code here
    stdata = sorted(data)
    stdata1 = stdata[0:len(stdata) // 2]
    stdata2 = stdata[len(stdata) // 2:]
    lengthdata = len(stdata)
    #print(stdata)
    #print(stdata1)
    #print(stdata2)

    if lengthdata % 2 == 0:
        #print(stdata1[-1])
        #print(stdata2[1])
        return (stdata1[-1] + stdata2[0]) / 2
    else:
        return stdata2[0]

print (median(data1))
print (median(data2))