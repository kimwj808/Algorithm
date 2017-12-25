def smallest(arr):
    sestnum=arr[0]
    sestindex=0
    for i in range(len(arr)):
        if arr[i]<sestnum:
            sestnum=arr[i]
    return sestnum
def smallsort(arr):
    smls=[]
    for i in range(len(arr)):
        sn=smallest(arr)
        arr.remove(sn)
        smls.append(sn)
    return smls

def smallest_book(arr):
    sestnum=arr[0]
    sestindex=0
    for i in range(1,len(arr)):
        if arr[i]<sestnum:
            sestnum=arr[i]
            #print sestindex
            sestindex=i
    return sestindex
def smallsort_book(arr):
    smls=[]
    for i in range(len(arr)):
        sn=smallest_book(arr)
        print sn
        smls.append(arr.pop(sn))
    return smls

ls=[0,9,3,2,8,1]
print smallsort_book(ls)
print smallsort(ls)
