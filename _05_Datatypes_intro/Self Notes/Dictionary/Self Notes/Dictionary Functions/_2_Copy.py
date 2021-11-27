# copy()------method returns a copy (shallow copy) of the dictionary

'''Copy ()------>It didn't modifies the original Dict'''

print("*****Copy*****")
print("Copy()--->Returns a copy of the dictionary")

a = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
print("Original Dict:", a)

b = a.copy()
print("Copied Dict:", b)