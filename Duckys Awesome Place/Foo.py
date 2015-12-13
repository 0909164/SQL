class Empty:
    def __init__(self):
        self.IsEmpty = True

    def __str__(self):
        return "[]"

class Node:
    def __init__(self, x, xs):
        self.IsEmpty = False
        self.Value = x
        self.Tail = xs

    def __str__(self):
        return str(self.Value) + "->" + str(self.Tail)

def range(start, end):
    lijst = Empty()
    while start <= end:
        end -= 1
        lijst = Node(end, lijst)
    return lijst

def foo(start,end):
    list = Empty()
    if start < end:
        list = Node(start,foo(start+1,end))
    else:
        list = Node(end,list)
    return list

print("Teacher Wrong Code")
print(range(1,3))
print("Awesome Ducky right Code")
print(foo(1,3))