
def findFirstNonRepeatingChar(s):

    # Edge cases Invalid Input
    if s == None or s == "":
        return -1


    """
    Can s have spaces? Can a space be considered as a non-repeating character? 
     Example " rahul" <-  If space is considered, ' ' would be the first non-repeating character
     
     """

    # Boundary cases
    if s == " " or len(s.strip()) == 1:
        return s

    counter = {}

    for char in s:
        if char.isspace() == False:
            counter[char] = counter.get(char,0)+1

    for char in s:
        if not char.isspace():
            if counter[char] == 1:
                print("Solution found : ", char)
                return char

    print("Every character is repeating. No solution to this.")
    return False


string = "this is the new shit"

findFirstNonRepeatingChar(string)