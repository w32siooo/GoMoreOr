import unittest

from GoMore import GoMore

class TestGoMore(unittest.TestCase):
    def setUp(self):
        self.myGoMore = GoMore()

class TestCreateRide(TestGoMore):
    def test_create_ride(self):

        #Check if length of rides list is correct after appending a trip.
        self.assertEqual(self.myGoMore.appendRide("Odense Copenhagen 2018-10-01 4".split()), 1)
        self.assertEqual(self.myGoMore.appendRide("Copenhagen Aarhus 2018-10-01 2".split()), 2)
        self.assertEqual(self.myGoMore.appendRide("Odense Copenhagen 2018-10-02 1".split()), 3)

class TestFindRide(TestGoMore):
    def test_find_ride(self):
        self.myGoMore.appendRide("Odense Copenhagen 2018-10-01 4".split())
        self.myGoMore.appendRide("Copenhagen Aarhus 2018-10-01 2".split())
        self.myGoMore.appendRide("Odense Copenhagen 2018-10-02 1".split())
        self.assertEqual('Odense Copenhagen 2018-10-01 4',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01".split()))
        self.assertEqual('Odense Copenhagen 2018-10-01 4 Odense Copenhagen 2018-10-02 1 ',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01 2018-10-03".split()))
        self.assertEqual('Odense Copenhagen 2018-10-01 4 ',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01 2018-10-03 2".split()))
        self.myGoMore.createReturnTrip('2018-10-03')
        self.assertEqual('Copenhagen Odense 2018-10-03 1',self.myGoMore.findRide(*"Copenhagen Odense".split()))





