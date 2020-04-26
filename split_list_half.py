def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

A = [0,1,2,3,4,5,6,7,8,9]

print(split_list(A, wanted_parts=2))
print(split_list(A, wanted_parts=3))
print(split_list(A, wanted_parts=8))


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5]
B, C = split_list(A)
print(B, C)