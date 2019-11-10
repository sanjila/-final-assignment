import unittest
from assignment import *
class Testassignment(unittest.TestCase):
    def test_search(self):
        root = Tk()
        frame = Student(root)
        # unit testing for first name
        frame.combo_search.set('First name')
        frame.entry_search.insert(0,'Sanjila')
        test_array=[(1, 'Sanjila', 'Shrestha', 'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                       (2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                       (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                       (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789),
                      ]
        expected_result1= [(1, 'Sanjila', 'Shrestha', 'BSc(Hons)Computing', 'Bhaktapur', 1234567890)]
        mylist = frame.info_search(test_array)
        self.assertEqual(mylist, expected_result1)


        # unit testing for last name
        frame.entry_search.delete(0, END)
        frame.combo_search.set('Last name')
        frame.entry_search.insert(0,'Shrestha')
        expected_result2 = [(1, 'Sanjila', 'Shrestha', 'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                            (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                            ]
        mylist = frame.info_search(test_array)
        self.assertEqual(mylist, expected_result2)

        # unit testing for student id
        frame.entry_search.delete(0, END)
        frame.combo_search.set('Student id')
        frame.entry_search.insert(0, '4')
        expected_result3= [(4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789),
                            ]
        mylist = frame.info_search(test_array)
        self.assertEqual(mylist, expected_result3)

        # unit testing for address
        frame.entry_search.delete(0, END)
        frame.combo_search.set('Address')
        frame.entry_search.insert(0, 'Kalimati')
        expected_result4= [(2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789)
                            ]
        mylist = frame.info_search(test_array)
        self.assertEqual(mylist, expected_result4)



if __name__ == '__main__':
    unittest.main()