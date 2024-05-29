a = 5
b = 10
def printer():
    global a, b
    a = "str"
    b = "str 2"
    c = 20
    d = 30
    print(c, d,"local")
    print(a, b, "global")

print(a, b)
printer()
print(a, b)

