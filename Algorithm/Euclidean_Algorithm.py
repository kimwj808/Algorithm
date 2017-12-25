def Euclidean_algorithm(a,b):
    if a<b:
        p=a
        a=b
        b=p
    if b==0:
        print (a,'k')
        return a
    else:
        print (a,b)
        return Euclidean_algorithm(b,a%b)

print Euclidean_algorithm(22222222,7772)


