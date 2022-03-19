from LINKED_LIST.linked_list_node import Node

class LinkedList:

    def __init__(self):
        self.start = None

    
    def add_node(self, data):

        if self.start == None:
            self.start = Node(data)
            return
            
        temp = self.start

        while temp.next != None:
            temp = temp.next

        temp.next = Node(data)


    def search_element(self, data):
        
        if self.start == None:
            return -1

        temp = self.start
        index = 0

        while temp.next != None and temp.data != data:
            temp = temp.next
            index = index + 1

        if temp.data == data:
            return index
        else:
            return -1

    def length_of_linked_list(self):

        if self.start == None:
            return 0

        temp = self.start
        length = 1

        while temp.next != None:
            temp = temp.next
            length = length + 1

        return length

    

        