def large_cont_sum(arr):
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array
    for num in arr[1:]:
        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum = max(current_sum, max_sum)

    return max_sum



def T_largest_cont_sum(fn,inputs,outputs):
    if len(inputs) != len(outputs) or fn == None:
        return -1

    all_passed = True
    for i in range(len(inputs)):
        if fn(inputs[i]) != outputs[i]:
            all_passed = False
            print(inputs[i])
            print(fn(inputs[i]))
            print(outputs[i])
            print("Test " + str(i) + " Failed")

    if all_passed:
        print("All tests successfully passed. Congrats!")

    return

inputs = [
[1, 2, -1, 3, 4, -1],
[1, 2, -1, 3, 4, 10, 10, -10, -1],
[-1, 1]
]
outputs = [9,29,12]

T_largest_cont_sum(large_cont_sum,inputs,outputs)

