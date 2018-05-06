# print([5] + [[2]])

def search(nums):
    prev = -1
    i = 0
    for num in nums:

        if num < prev:
            break
        prev = num
        i += 1

    if prev == None:
        i = 0

    pivot_index = i
    print(pivot_index)


search([5,6,7,1,2,3,4])