from insertion import LinkedList

class Rotate(LinkedList):
    def rotate(self,pivot):
        start = self.head
        cur_node =self.head
        counter = 1
        while counter < pivot:
            cur_node = cur_node.next
            counter +=1
        rotate_node = cur_node.next
        cur_node.next = None
        self.head = rotate_node
        while rotate_node.next:
            rotate_node = rotate_node.next
        rotate_node.next = start

linked_list = Rotate()

for i in range(1,13):
    linked_list.append(i)

linked_list.print()

linked_list.rotate(4)

linked_list.print()
