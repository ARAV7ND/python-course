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

    def print(self):
        point = self.head
        while(point!=None):
            print(point.data,"->",end='')
            point = point.next
        print()
    def length(self):
        cur_node = self.head
        len = 0
        while cur_node :
            cur_node  = cur_node.next
            len +=1
        return len

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)
    linked_list.append(6)
    linked_list.print()
    print('len = ',linked_list.length())