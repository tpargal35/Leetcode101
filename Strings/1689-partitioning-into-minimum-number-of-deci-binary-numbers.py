def minPartitions(n: str) -> int:
    # no docstring. If you need 1, maybe try another hobby.
    maxi = 0
    for i in n:
        if int(i) > maxi: 
            maxi = int(i)
    return maxi 

print(minPartitions("32"))