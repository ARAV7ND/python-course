# append
# prepend
# insert_after_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        print('initialized')
        self.head=None
    def append(self,data):
        print('append')
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
        cur_node = self.head
        if self.head ==None:
            self.head = node
            return
        if( index==0):
            node.next = self.head
            self.head = node
            return
        while(i<index and cur_node):
            i+=1
            cur_node = cur_node.next
        if i == index:
            node.next = cur_node.next
            cur_node.next = node

    def delete_node(self,key):
        cur_node = self.head

        if(cur_node and cur_node.data == key):
            self.head = cur_node.next
            cur_node = None
            return
        prev = None

        while(cur_node and cur_node.data != key):
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_position(self, index):
        cur_node = self.head
        if index <0 or  cur_node is None:
            return
        if index == 0 and cur_node:
            self.head = cur_node.next
            cur_node = None
        cur_pos = 0
        prev = None
        while cur_node and cur_pos < index :
            cur_pos += 1
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
        

    def print(self):
        point = self.head
        while(point!=None):
            print(point.data,"->",end='')
            point = point.next
        print()
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(6)
linked_list.prepend(0)
linked_list.insert_after_node(0,-1)
linked_list.insert_after_node(4,5)
linked_list.insert_after_node(3,3)
linked_list.print()
linked_list.delete_node(3)
linked_list.print()
linked_list.delete_node(-1)
linked_list.print()
linked_list.delete_node(6)
linked_list.print()
linked_list.delete_position(0)
linked_list.print()
linked_list.delete_position(2)
linked_list.print()
linked_list.delete_position(2)
linked_list.print()