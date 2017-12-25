def binary_search(ls,num):
    #print ls
    fir=ls[0]
    last=ls[-1]
    ban=(fir+last)/2
    print ban,num
    if ban > num:
        binary_search(range(fir,ban+1),num)
    elif num > ban:
        binary_search(range(ban,last+1),num)
    elif num==ban:
        print ls,ban
        return ban
ls=range(1,22)
print 'l',binary_search(ls,10)
print len(ls)
print ls[20]
def bisearch(ls,item):
    low=0
    high=len(ls)-1

    while low<=high:
        mid = (low + high) / 2
        guess = ls[mid]
        if guess==item:
            return mid
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    else:
        return 'Not found'
print 'o',bisearch(range(1,51),22)
#1,50  10
#b 25 n 10
#1 25 10
#13 10
#1 13 10
#7 10
#7 13
#10 10