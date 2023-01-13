from insertion import LinkedList

class RemoveDuplicates(LinkedList):
    def __init__(self):
        super().__init__()
        self.entries = dict()
    def remove_duplicates(self):
        if not self.head:
            return
        cur_node = self.head
        prev = None
        while cur_node :
            if cur_node.data in  self.entries:
                prev.next = cur_node.next
                cur_node = cur_node.next
            else:
                self.entries[cur_node.data] = 1
                prev = cur_node
                cur_node = cur_node.next
linked_list = RemoveDuplicates()

for i in range(10):
    linked_list.append(i)
    linked_list.append(i)

linked_list.print()
linked_list.remove_duplicates()
linked_list.print()
