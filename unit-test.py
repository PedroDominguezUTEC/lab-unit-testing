from pickle import FALSE
import unittest

from sqlalchemy import true
from unit import Verificador, DateException, DateFormatException


class test(unittest.TestCase):
    def test_cases(self):

        res = Verificador('01-01-1992', '01-01-1992').determinar_mayoria_edad()
        self.assertEqual(res, False)

        res = Verificador('01-01-1992', '01-01-2022').determinar_mayoria_edad()
        self.assertEqual(res, True)

        self.assertRaises(DateException, lambda: Verificador('01-01-2022', '01-01-1992').determinar_mayoria_edad())
        self.assertRaises(DateFormatException, lambda: Verificador('01-01-201zxcv22', '01-01-19192').determinar_mayoria_edad())


        self.assertRaises(DateFormatException, lambda: Verificador('01-0331-201-zxcv-22', '01-01-19192').determinar_mayoria_edad())
        self.assertRaises(DateFormatException, lambda: Verificador('01-0101010101-2011', '01-01-19192').determinar_mayoria_edad())
if __name__ == '__main__':
    unittest.main()