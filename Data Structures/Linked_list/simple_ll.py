class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_in_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def prints(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        

        itr = self.head
        ll_str = ''

        while itr:
            ll_str += str(itr.data) + "--->"
            itr = itr.next

        print(ll_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def insert_list_values(self, data_list):
        # self.head = None (to insert from start)
        for i in data_list:
            self.insert_at_end(i)


    def get_length(self):
        itr = self.head
        
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    

    def remove_element(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_in_beginning(data)
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1



if __name__ == "__main__":
    ll = linkedlist()
    ll.insert_in_beginning(40)
    ll.insert_in_beginning(50)
    ll.insert_at_end(22)
    ll.insert_list_values([12,45,23,78,98,80])
    ll.remove_element(3)
    ll.insert_at(3,90)
    ll.prints()
    print("The length of the LinkedList is: ",ll.get_length())



