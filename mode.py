data1 = [1,2,5,10,-20,5,5]

def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode

print mode(data1)



data1=[1,2,5,10,-20,5,5]

def mode(data):
    #Insert your code here
    mode_count= 0
    for item in range(len(data)):
        item_count = data.count(data[item])
        if item_count > mode_count:
            mode = data[item]
            mode_count = item_count
    return mode

print mode(data1)
