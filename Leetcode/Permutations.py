
def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        permutations_list = []
        for i in range(len(s)):
            element = s[i]


            for perm in permutations(s[:i] + s[i+1:]):
                permutations_list+= [element + perm]
        return permutations_list

print(permutations("abc"))

