"""
Python is a High Level Language and offers a layer of abstraction over the primitive data-types such that it is easy to translate complex business problems seamlessly.

However, there is a trade-off with efficiency sometimes and the space and time complexieties of the programs are neglected.

This program aims to uncover the size of the different data-types and data structures used in python.

"""


import sys
arr = [i*10 for i in range(1)]
test_elements = [1,
                 3.3,
                 True,
                 "",
                 "Name",
                 [],
                 arr,
                 {},
                 {1:'a',2 : 'c'}]


for element in test_elements:
    print("Size of " + str(element) + " ----------------> ", sys.getsizeof(element))


""" Sorted method uses  "TimSort" ->>>>>> O[nlog(n)] Time complexity and  """