
s = "rahulisgreat"

def getName(fn):
    if not callable(fn):
        print("Not a function")
    else:
        print("A funciton")

def get():
    pass

getName(get)
# print("A Function:" ,callable(getNames))

print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())

s = "r10a"
print(s.isalnum())

s = "10"
print(s.isnumeric())
print(s.isdigit())
print(s.isalpha())


print()
print()
print()
a = [1,2,3,4]
print(str(a))
# a = map(a,str)
print(" ".join(str(a)))

print("rahul ".strip().split(" "))