from length import LinkedList

class NthToLast(LinkedList):
    def nthToLast(self,n):
        len = self.length()
        cur_node = self.head
        i = 0
        while i + n <len and cur_node:
            cur_node = cur_node.next
            i+=1
        while(cur_node):
            print(cur_node.data,'->',end='')
            cur_node = cur_node.next
    def nthToLastEff(self, n):
        #move n for first pointer , then move both pointers
        p = self.head
        q = self.head
        move_n =0
        while p and move_n <n:
            p = p.next
            move_n +=1
        while p :
            q = q.next
            p = p.next
        while q:
            print(q.data,'->',end='')
            q = q.next


linked_list = NthToLast()


for i in range(10):
    linked_list.append(i)
linked_list.print()
linked_list.nthToLast(10)
print()
linked_list.nthToLastEff(5)