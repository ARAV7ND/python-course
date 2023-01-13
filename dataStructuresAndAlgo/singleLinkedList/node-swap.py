from insertion import LinkedList

class NodeSwap(LinkedList):
    def __init__(self):
        super().__init__()
    
    def swap(self, i, j):
        cur_node = self.head
        if(i == j):
            return
        if i>j:
            i,j = j,i
        key1 = 0
        key2 = 0
        prev1 = None
        while cur_node and key1<i:
            prev1 = cur_node
            cur_node = cur_node.next
            key1+=1
        prev2 = None
        cur_node2 = self.head
        while cur_node2 and key2<j:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
            key2+=1  
        if not cur_node or not cur_node2 :
            return                    
        if prev1:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        
        if prev2:
            prev2.next = cur_node
        else:
            self.head = cur_node
        
        cur_node.next , cur_node2.next = cur_node2.next , cur_node.next


linked_list = NodeSwap()
linked_list.append(2)
linked_list.append(3)
linked_list.swap(0,1)
linked_list.print()
# linked_list.append(3)
# linked_list.print()
# linked_list.swap(0,1)
# linked_list.print()
# linked_list.append(1)
# linked_list.append(4)
# linked_list.print()
# linked_list.swap(0,3)
# linked_list.print()
# linked_list.append(5)
# linked_list.append(6)
# linked_list.print()
# linked_list.swap(1,4)
# linked_list.print()



            
