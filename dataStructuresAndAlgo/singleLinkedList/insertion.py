# append
# prepend
# insert_after_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        node = Node(data)
        if(self.head ==None):
            self.head = node
            return
        point = self.head
        while(point.next !=None):
            point = point.next
        point.next = node

    def prepend(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after_node(self,index,data):
        node = Node(data)
        i=0
        point = self.head
        if self.head ==None:
            self.head = node
            return
        if( index==0):
            node.next = self.head
            self.head = node
            return
        while(i<index and point!=None):
            i+=1
            point = point.next
        if(i == index):
            node.next = point.next
            point.next = node


    def print(self):
        point = self.head
        while(point!=None):
            print(point.data,"->",end='')
            point = point.next
        print()

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)
    linked_list.print()
    linked_list.prepend(0)
    linked_list.print()
    linked_list.insert_after_node(0,-1)
    linked_list.print()
    linked_list.insert_after_node(4,5)
    linked_list.print()
    linked_list.insert_after_node(3,3)
    linked_list.print()
