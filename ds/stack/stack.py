 
class stack:
    def __init__(self):
        self.arr=[]
        self.top=-1
    
    # push

    def push(self,element):
        self.top+=1
        self.arr.append(element)

    def print(self):
        if (self.isEmpty()):  # 1
            print("Stack is empty")
        else:  # 0
            for i in range(len(self.arr)):
                print(self.arr[i])
    
    def isEmpty(self):
        if self.size()==0:
            return 1
        else:
            return 0
        
    def size(self):
        return self.top+1


    def pop(self):
        if (self.isEmpty()):
            print("Pop can't be done in empty stack")
        else:
            print("Popped element is ", self.arr[self.top])
            self.arr.pop()
            self.top-=1


    def topElement(self):
        if self.isEmpty(): 
            print("Stack is empty so no top element")
        else:
            return self.arr[self.top]
    

# if "__name__"=="__main__":
k=stack()
k.push(2)
# k.print()
k.push(5)
k.push(6)
k.push(7)
k.print()
print("This is the top element")
print(k.topElement())
k.pop()
k.print()

# Applications -> infix to postfix , parenthsis checker , evaluation of prefix , postfix in single scan