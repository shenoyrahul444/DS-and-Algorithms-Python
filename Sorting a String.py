def partition(slist, low , high):
    if low < high:
        i = (low - 1)
        pivot = slist[high]

        for j in range(low,high):
            if slist[j] <= pivot:
                i+= 1
                slist[i],slist[j] = slist[j],slist[i]
        slist[i+1],slist[high] = slist[high],slist[i+1]

        return (i+1)

def quicksort(slist,low,high):
    if low < high:
        pi = partition(slist,low,high)
        quicksort(slist,low,pi-1)
        quicksort(slist,pi+1,high)

def sortString(s):


    slist = []
    n = 0
    for i in s:
        slist.append(ord(i))
        n += 1

    quicksort(slist,0,n-1)

    for i in range(n):
        slist[i] = chr(slist[i])

    return "".join(slist)


name = "Rahulisgreat"
sorted_name = sortString(name)
print(sorted_name == "".join(sorted(name)))
