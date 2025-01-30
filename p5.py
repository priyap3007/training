l=["A",-20,"a",94,66]
l.sort(key=lambda x:(isinstance(x,int),x))
print(l)