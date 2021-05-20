import unittest

from GoMore import GoMore

#The following testclass is for the non firebase version of the program.
class TestGoMore(unittest.TestCase):
    def setUp(self):
        self.myGoMore = GoMore()
        self.myGoMore.appendRide("Odense Copenhagen 2018-10-01 4".split())
        self.myGoMore.appendRide("Copenhagen Aarhus 2018-10-01 2".split())
        self.myGoMore.appendRide("Odense Copenhagen 2018-10-02 1".split())

#Insert the three rides that make the base for our tests.
class TestCreateRide(TestGoMore):
    def test_create_ride(self):
        #Check if length of rides list is correct after appending a trip.
        self.assertEqual(self.myGoMore.appendRide("Odense Copenhagen 2018-10-01 4".split()), 4)
        self.assertEqual(self.myGoMore.appendRide("Copenhagen Aarhus 2018-10-01 2".split()), 5)
        self.assertEqual(self.myGoMore.appendRide("Odense Copenhagen 2018-10-02 1".split()), 6)

#Testing the findRide function. Expected output should match the search string.
class TestFindRide(TestGoMore):
    def test_find_ride(self):
        self.assertEqual('Odense Copenhagen 2018-10-01 4',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01".split()))
        self.assertEqual('Odense Copenhagen 2018-10-01 4 Odense Copenhagen 2018-10-02 1 ',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01 2018-10-03".split()))
        self.assertEqual('Odense Copenhagen 2018-10-01 4 ',self.myGoMore.findRide(*"Odense Copenhagen 2018-10-01 2018-10-03 2".split()))

        #Create the return trip.
        self.myGoMore.createReturnTrip('2018-10-03')

        #Test if the return trip is working with the correct expected return date.
        self.assertEqual('Copenhagen Odense 2018-10-03 1',self.myGoMore.findRide(*"Copenhagen Odense".split()))





