from BINARY_SEARCH import search_methods            #module to test
import unittest                                     #The test framework

class Test_BinarySearch(unittest.TestCase):
    def test_search(self):
        result = search_methods.search([1,2,3,4,5,6,7,8,9], 1)
        self.assertEqual(result, 0)

        result = search_methods.search([1,2,3,4,5,6,7,8,9], 9)
        self.assertEqual(result, 8)

        result = search_methods.search([1,2,3,4,5,6,7,8,9], 5)
        self.assertEqual(result, 4)

        result = search_methods.search([1,2,3,4,5,6,7,8,9], 11)
        self.assertEqual(result, -1)

        result = search_methods.search([], 1)
        self.assertEqual(result, -1)



    def test_bs_present(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 1)
        self.assertEqual(result, 1)

    def test_bs_not_present(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 11)
        self.assertEqual(result, -1)

    def test_bs_present_list_size1(self):
        result = search_methods.binary_search([0], 0, 0, 0)
        self.assertEqual(result, 0)

    def test_bs_not_present_list_size1(self):
        result = search_methods.binary_search([0], 0, 0, 1)
        self.assertEqual(result, -1)

    def test_bs_not_present_empty_list(self):
        result = search_methods.binary_search([], 0, 0, 1)
        self.assertEqual(result, -1)
    
    def test_bs_present_middle_even_list_size(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 5)
        self.assertEqual(result, 5)

    def test_bs_present_middle_odd_list_size(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8], 0, 8, 5)
        self.assertEqual(result, 5)

    def test_bs_present_end_even_list_size(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 9)
        self.assertEqual(result, 9)
    
    def test_bs_present_end_odd_list_size(self):
        result = search_methods.binary_search([0,1,2,3,4,5,6,7,8], 0, 8, 8)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()