#To initialize Node whenever user pushes new element
class Node:
    def __init__(self,item):
        self.data = item
        self.__next = None

#Contains push[insert], pop[delete], top[topmost element in Stack], IsEmpty[True or False], Size[Element Size] of the Linked list using Stack Approach
class StackLL:
    
    def __init__(self):
        self.__head = None
        self.__count = 0
        
    def push(self,item):
        if self.__head is None:
            newNode = Node(item)
            self.__head = newNode
            self.__count = self.__count + 1
            return self.__head
        else:
            newNode = Node(item)
            newNode.__next = self.__head
            self.__head = newNode
            self.__count = self.__count + 1
            return self.__head
    
    def pop(self):
        if self.IsEmpty():
            print("Hey, Stack is Empty!!")
            return
        else:
            data = self.__head.data
            self.__head = self.__head.__next
            self.__count = self.__count - 1
            return data
    def top(self):
        if self.IsEmpty():
            print("Hey, Stack is Empty!!")
            return
        return self.__head.data
        
    def size(self):
        return self.__count
        
    def IsEmpty(self):
        return self.size() == 0

#***************************************** INPUTS ************************************************#
# s = StackLL()
# s.push(5)
# s.push(4)
# print(s.pop())
# s.push(3)
# print(s.IsEmpty())
# print(s.size())
# print(s.top())

#*************************************** OUTPUT ***********************************************#
# 4
# False
# 2
# 3
