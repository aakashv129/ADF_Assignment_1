import unittest
import day_5_ass as d


class check(unittest.TestCase):
    d.v.__init__()

    def test_fname(self):
        k, m = d.v.f_name_checker("anand")
        self.assertEqual(k, 0)

    def test_mname(self):
        k, m = d.v.f_name_checker("anand")
        self.assertEqual(k, 0)

    def test_lname(self):
        k, m = d.v.f_name_checker("anand")
        self.assertEqual(k, 0)

    def test_gender(self):
        k, m = d.v.f_name_checker("Male")
        self.assertEqual(k, 0)

    def test_city(self):
        k, m = d.v.f_name_checker("coimbatore")
        self.assertEqual(k, 0)

    def test_state(self):
        k, m = d.v.f_name_checker("Andhra Pradesh")
        self.assertEqual(k, 0)

    def test_pincode(self):
        k, m = d.v.f_name_checker(678956)
        self.assertEqual(k, 0)

    def test_salary(self):
        k, m = d.v.f_name_checker(9999)
        self.assertEqual(k, 0)

if __name__=='__main__':
    c = check()
    c.test_fname()
    c.test_mname()
    c.test_gender()
    c.test_salary()
    c.test_pincode()
    c.test_city()
    c.test_lname()
    c.test_state()
