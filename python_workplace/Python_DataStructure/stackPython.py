
# Stack in Python can be implemented using the following ways: 

#     list
#     Collections.deque
#     queue.LifoQueue

class stack:
    def __init__(self):
        self.array=[] 
        self.top=-1
        self.max=100   


    def isEmpty(self):
        if self.top== -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top==self.max-1:
            return True
        else:
            return False

    def push(self,data):
        if self.isFull():
            print("Stack is overflow...")
        else:
            self.top +=1
            self.array.append(data) 


    def pop(self):
        if self.isEmpty():
            print("stack is underflow....")                       
            return
        else:
            self.top -=1
            return self.array.pop()


class StackOper(stack):
    def push(self,x):
        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)    
            y=self.Min.pop()
            self.Min.push(y)
            if x<=y:
                self.Min.push(x)
            else:
                self.Min.push(y)    


    def pop(self):
        x=super().pop()
        self.Min.pop()
        return x



    def getmin(self):
        x=self.Min.pop()
        self.Min.push(x)    
        return x

if __name__=='__main__':
    child=StackOper()
    child.push(10)
    child.push(20)
    child.push(30)
    print(child.getmin())

    child.pop(20)




























