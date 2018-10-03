def birthday(iteration,p,d=365):
    '''
    iterations - how many times the function will process the data.
    !!! If you set iterations number > 100 000 it will think very slow
    (2 min on my PC).
    p - how many people are in a group,
    d - the number of days
    Function return probability of two and more people have the same birthdays
    '''
    from random import randint
    count = 0
    for i in range(iteration):
        bth = []
        adubl = 0
        for j in range(p):
            bth.append(randint(1,d))
        for s in range(len(bth)):
            for y in range(len(bth)):
                if s == y:
                    continue
                elif bth[s] == bth[y]:
                    adubl+=0.5
        if adubl !=0:
            count+=1
    chanse =  (count/iteration)*100
    return chanse