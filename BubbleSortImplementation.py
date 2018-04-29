
def bubblesort(alist):

    n = len(alist)
    for i in range(n):
        for j in range(0,n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1] , alist[j]


alist = [7,1,9,3,5,2,3,8,1]
print(alist)
bubblesort(alist)
print(alist)