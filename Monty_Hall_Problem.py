from random import randint

N = 1000

def simulate(N):
    K = 0
    ###insert your code here###
    for i in range(N):
        truth = randint(1, 3)
        guess1 = randint(1, 3)
        if guess1 == truth:
            monte = randint(1, 3)
            while monte == truth:
                monte = randint(1, 3)
        else:
            monte = 6 - guess1 -truth
        guess2 = 6 - guess1 - monte
        if guess2 == truth:
            K = K + 1
    return float(K) / float(N)

print (simulate(N))