def binary_search(ls, num):
    # helper function to search the indices
    # we "know" ls and num from the outer-scope, so we'll pass only the indices
    def search(first=0, last=len(ls)):
        if first < last:
            mid = (first + last) // 2
            ban = ls[mid]
            if ban > num:
                return search(first, mid-1)
            elif num > ban:
                return search(mid+1, last)
            elif num == ban:
                return mid  # return the index - not the number itself!
        else:
            return "not found!"
    return search()


ls = range(1,22)  # you should wrap range with list!
print(binary_search(ls, 10))
print(binary_search(ls, 33))
