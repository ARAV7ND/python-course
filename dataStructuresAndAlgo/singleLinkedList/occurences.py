from insertion import LinkedList

class Occ(LinkedList):
    def occurences(self,n):
        occ = dict()
        cur_node =self.head
        while cur_node:
            if cur_node.data in occ:
                occ[cur_node.data] +=1
            else:
                occ[cur_node.data] =1
            cur_node = cur_node.next
        return occ[n]
linked_list = Occ()

for i in range(14):
    linked_list.append(i)
    linked_list.append(i)
    linked_list.append(i)
linked_list.append(2)
linked_list.print()

print('occ of 1',linked_list.occurences(2))