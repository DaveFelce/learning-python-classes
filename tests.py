import unittest
from adder import Adder, DictAdder, ListAdder
from attrs import Attrs

@unittest.skip("Blah..")
class AdderTest(unittest.TestCase):

    def test_adder(self):
        a = Adder(data=[])
        self.assertRaises(NotImplementedError, a.add, [])

    def test_list_adder(self):
        a = [1,2,3]
        ladder = ListAdder(data=a)
        b = [4,5,6]
        c = ladder + b
        self.assertEqual(c, [1,2,3,4,5,6])

    def test_dict_adder(self):
        a = {'one': 'two'}
        dadder = DictAdder(data=a)
        b = {'3': 4}
        c = dadder + b
        self.assertEqual(c, {'one': 'two', '3': 4})


class AttrTest(unittest.TestCase):

    def test_attrs(self):
        a = Attrs()

        a.thing = 'thing'
        self.assertEqual(a.thing, 'thing')
        self.assertEqual(a.stuff, 'HELLO DAVE')
        self.assertEqual(a.pants, 'HELLO DAVE')


if __name__ == '__main__':
    unittest.main()


