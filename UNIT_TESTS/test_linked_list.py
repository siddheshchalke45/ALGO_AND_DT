from LINKED_LIST.linked_list import LinkedList
from LINKED_LIST.linked_list_node import Node
import unittest

class Test_LinkedList(unittest.TestCase):

    def test_search_node_int(self):

        self.linked_list = LinkedList()
        self.linked_list.add_node(1)
        self.linked_list.add_node(2)
        self.linked_list.add_node(3)
        self.linked_list.add_node(4)
        self.linked_list.add_node(5)

        result = self.linked_list.search_element(1)
        self.assertEqual(result, 0)

        result = self.linked_list.search_element(5)
        self.assertEqual(result, 4)

        result = self.linked_list.search_element(3)
        self.assertEqual(result, 2)

        result = self.linked_list.search_element(8)
        self.assertEqual(result, -1)


    def test_search_node_string(self):

        self.linked_list = LinkedList()
        self.linked_list.add_node("Sid")
        self.linked_list.add_node("Saurabh")
        self.linked_list.add_node("Vishal")
        self.linked_list.add_node("Prashant")
        self.linked_list.add_node("Sam")

        result = self.linked_list.search_element("Sid")
        self.assertEqual(result, 0)

        result = self.linked_list.search_element("Sam")
        self.assertEqual(result, 4)

        result = self.linked_list.search_element("Vishal")
        self.assertEqual(result, 2)

        result = self.linked_list.search_element("John")
        self.assertEqual(result, -1)


    def test_length_of_linked_list(self):
        self.linked_list = LinkedList()

        result = self.linked_list.length_of_linked_list()
        self.assertEqual(result, 0)

        self.linked_list.add_node(1)
        result = self.linked_list.length_of_linked_list()
        self.assertEqual(result, 1)

        self.linked_list.add_node(2)
        self.linked_list.add_node(3)
        self.linked_list.add_node(4)
        self.linked_list.add_node(5)
        result = self.linked_list.length_of_linked_list()
        self.assertEqual(result, 5)

        self.linked_list.add_node(2)
        self.linked_list.add_node(3)
        self.linked_list.add_node(4)
        self.linked_list.add_node(5)
        result = self.linked_list.length_of_linked_list()
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()