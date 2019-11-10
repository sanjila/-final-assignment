import unittest
from assignment import *
import tkinter
class Testassignment(unittest.TestCase):
    def test_sort(self):
        test_array=[(1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                    (2,'Ruby', 'Rai',  'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                    (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                    (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789)]

        #unit testing for sorting student id

        expected_result = [(1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                    (2,'Ruby', 'Rai',  'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                    (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                    (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789)]
        root=Tk()
        frame= Student(root)
        frame.combo_sort.set('Student id')

        frame.Quick_sort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, expected_result)

        # unit testing for sorting first name
        frame.combo_sort.set('First name')
        expected1=[(3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                   (2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                   (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789),
                   (1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890)]
        frame.Quick_sort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, expected1)

        # unit testing for sorting last name
        frame.combo_sort.set('Last name')
        expected2=[(4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789),
                   (2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                   (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                   (1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890)]
        frame.Quick_sort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, expected2)

        # unit testing for sorting degree
        frame.combo_sort.set('Degree')
        expected3=[ (1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                    (2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                    (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                    (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789)
                     ]
        frame.Quick_sort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, expected3)

        # unit testing for sorting address
        frame.combo_sort.set('Address')
        expected4=[ (1,'Sanjila', 'Shrestha',  'BSc(Hons)Computing', 'Bhaktapur', 1234567890),
                    (3, 'Mahima', 'Shrestha', 'Msc.It', 'Chahbil', 1223345678),
                    (2, 'Ruby', 'Rai', 'BSc(Hons)Ethical Hacking', 'Kalimati', 1203456789),
                    (4, 'Sandhya', 'Khatri', 'Msc.software engineering', 'Maitidevi', 2213456789)
                     ]
        frame.Quick_sort(test_array, 0, len(test_array) - 1)
        self.assertEqual(test_array, expected4)



if __name__ == '__main__':
    gui = Tk()
    root = Student(gui)
    unittest.main()