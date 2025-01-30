def ASCII(x):
    if type(x)==str:
        return ord(x)
    return(x)
sort=["A",-20,"a",94,66]
sort.sort(key=ASCII)
print(sort)