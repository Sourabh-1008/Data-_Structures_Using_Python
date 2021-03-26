class stack:
    def __init__(self):
        self.list = []


    def push(self, item):
        self.list.append(item)
        

    def pop(self):
        self.list.pop()
        
    def tos(self):
        print(self.list[len(self.list)-1])

    def traverse(self):
        for i in self.list:
            print(i,end=" ")


s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

s1.traverse()
print("\n")
s1.pop()
s1.pop()
print("\n")
s1.traverse()
print("\n")
s1.tos()


