from insertion import LinkedList

class Reverse(LinkedList):
    
    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node:
            temp = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = temp
        self.head = prev
    def reverse_recursive(self):
        def reverse_recurse(cur_node,prev):
            if not cur_node:
                return prev
            temp = cur_node.next
            cur_node.next= prev
            return reverse_recurse(temp,cur_node)

        self.head = reverse_recurse(self.head,None)
        
    
linked_list = Reverse()
for i in range(0,9):
    linked_list.append(i)
linked_list.print()
linked_list.reverse_recursive()
linked_list.print()
            