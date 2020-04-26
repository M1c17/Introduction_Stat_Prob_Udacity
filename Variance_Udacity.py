data2 = [13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu = mean(data)
    return mu([(i-mu)**2 for i in data])

print(variance(data2))