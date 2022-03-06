from LINKED_LIST.linked_list import LinkedList
from LINKED_LIST.linked_list_node import Node
import unittest

class Test_LinkedList(unittest.TestCase):

    def test_search_node(self):

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


if __name__ == '__main__':
    unittest.main()