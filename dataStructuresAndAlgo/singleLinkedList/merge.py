from insertion import LinkedList

class Merge(LinkedList):

    def merge(self, linked_list):
        p = self.head
        q = linked_list.head
        s = None
        if  not q :
            return
        if p and p.data <= q.data:
            s = self.head
            p = p.next
        else:
            s = q
            q = q.next
            self.head = s
        while p or q :
            if  (p and q and p.data <= q.data) or (p and not q):
                s.next = p
                s = p
                p = p.next
            elif q:
                s.next = q
                s = q
                q = q.next
        if p:
            s.next = p
            s =p
            s.next = None
        if q:
            s.next = q
            s = q
            s.next = None
linked_list = Merge()

linked_list.append(1)
linked_list.append(5)
linked_list.append(7)
linked_list.append(9)
linked_list.append(10)
# for i in range(0,16,2):
#     linked_list.append(i)

linked_list2 = Merge()

# for i in range(1,16,2):
#     linked_list2.append(i)
linked_list2.append(2)
linked_list2.append(3)
linked_list2.append(4)
linked_list2.append(6)
linked_list2.append(8)
linked_list.merge(linked_list2)
linked_list.print()