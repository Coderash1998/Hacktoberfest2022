class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp =temp.next
            
    def insertAt(self, newelement, position):
        newnode = Node(newelement)
        if position<1:
            print("unable to do so")
        elif position == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            for i in range(1, position-1):
                if temp != None:
                    temp = temp.next
            if (temp != None):
                newnode.next = temp.next
                temp.next =newnode
            else:
                print("Previous node is null")

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False


    def lengthList(self,p):
       
        t=self.head
        c=0
        while(t):
           c+=1
           t=t.next

        if p>c:
            return False
        
        t=self.head
        x=c-p
        print("value is ",x)
        while(x>0):
            x-=1
            t=t.next
        return t.data
    
    def push(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode


if __name__=='__main__':
    
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    
    llist.head.next = second 
    second.next = third 
    third.next = fourth
    fourth.next = fifth

    
    llist.printList()
    llist.insertAt(6,1)

    print()
    llist.printList()

    
    print()
    print(llist.lengthList(2))
    
    '''
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    llist.printList()
    llist.head.next.next.next.next = llist.head
    if(llist.detectLoop()):
        print("Loop found")
    else:
        print("No Loop ")
    '''
