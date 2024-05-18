import unittest
from sl_list import ListeSC


class ListeSC_Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.lvide = ListeSC()
        self.lsingleton = ListeSC([1])
        self.ldeux = ListeSC([1, 2])
        self.ltrois = ListeSC([1, 2, 3])
        self.l10 = ListeSC([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_construction(self):
        self.assertEqual("[]", self.lvide.__str__())
        self.assertEqual("[1]", self.lsingleton.__str__())
        self.assertEqual("[1, 2]", self.ldeux.__str__())
        self.assertEqual("[1, 2, 3]", self.ltrois.__str__())

    def test_len(self):
        self.assertEqual(0, len(self.lvide))
        self.assertEqual(1, len(self.lsingleton))
        self.assertEqual(2, len(self.ldeux))
        self.assertEqual(3, len(self.ltrois))

    def test_inserer_premier(self):
        self.lvide.inserer_premier(10)
        self.assertEqual("[10]", self.lvide.__str__())
        self.assertEqual(1, len(self.lvide))
        self.lsingleton.inserer_premier(10)
        self.assertEqual("[10, 1]", self.lsingleton.__str__())
        self.assertEqual(2, len(self.lsingleton))
        self.ldeux.inserer_premier(10)
        self.assertEqual("[10, 1, 2]", self.ldeux.__str__())
        self.assertEqual(3, len(self.ldeux))
        self.ltrois.inserer_premier(10)
        self.assertEqual("[10, 1, 2, 3]", self.ltrois.__str__())
        self.assertEqual(4, len(self.ltrois))

    def test_inserer_dernier(self):
        self.lvide.inserer_dernier(10)
        self.assertEqual("[10]", self.lvide.__str__())
        self.assertEqual(1, len(self.lvide))
        self.lsingleton.inserer_dernier(10)
        self.assertEqual("[1, 10]", self.lsingleton.__str__())
        self.assertEqual(2, len(self.lsingleton))
        self.ldeux.inserer_dernier(10)
        self.assertEqual("[1, 2, 10]", self.ldeux.__str__())
        self.assertEqual(3, len(self.ldeux))
        self.ltrois.inserer_dernier(10)
        self.assertEqual("[1, 2, 3, 10]", self.ltrois.__str__())
        self.assertEqual(4, len(self.ltrois))

    def test_retirer_dernier(self):
        self.assertEqual(None, self.lvide.retirer_dernier())
        self.assertEqual("[]", self.lvide.__str__())
        self.assertEqual(0, len(self.lvide))
        self.assertEqual(1, self.lsingleton.retirer_dernier())
        self.assertEqual("[]", self.lsingleton.__str__())
        self.assertEqual(0, len(self.lsingleton))
        self.assertEqual(2, self.ldeux.retirer_dernier())
        self.assertEqual("[1]", self.ldeux.__str__())
        self.assertEqual(1, len(self.ldeux))
        self.assertEqual(3, self.ltrois.retirer_dernier())
        self.assertEqual("[1, 2]", self.ltrois.__str__())
        self.assertEqual(2, len(self.ltrois))

    def test_retirer_premier(self):
        self.assertEqual(None, self.lvide.retirer_premier())
        self.assertEqual("[]", self.lvide.__str__())
        self.assertEqual(0, len(self.lvide))
        self.assertEqual(1, self.lsingleton.retirer_premier())
        self.assertEqual("[]", self.lsingleton.__str__())
        self.assertEqual(0, len(self.lsingleton))
        self.assertEqual(1, self.ldeux.retirer_premier())
        self.assertEqual("[2]", self.ldeux.__str__())
        self.assertEqual(1, len(self.ldeux))
        self.assertEqual(1, self.ltrois.retirer_premier())
        self.assertEqual("[2, 3]", self.ltrois.__str__())
        self.assertEqual(2, len(self.ltrois))

    def test_retirer_position(self):
        self.assertEqual(1, self.lsingleton.retirer_position(0))
        self.assertEqual("[]", self.lvide.__str__())
        self.assertEqual(0, len(self.lsingleton))
        self.ldeux.retirer_position(0)
        self.assertEqual("[2]", self.ldeux.__str__())
        self.ltrois.retirer_position(2)
        self.assertEqual("[1, 2]", self.ltrois.__str__())
        self.assertEqual(7, self.l10.retirer_position(6))
        self.assertEqual("[1, 2, 3, 4, 5, 6, 8, 9, 10]", self.l10.__str__())
        self.assertEqual(2, self.l10.retirer_position(1))
        self.assertEqual("[1, 3, 4, 5, 6, 8, 9, 10]", self.l10.__str__())
        self.assertEqual(10, self.l10.retirer_position(7))
        self.assertEqual("[1, 3, 4, 5, 6, 8, 9]", self.l10.__str__())

    def test_ajouter_position(self):
        self.lvide.inserer_position(0, 42)
        self.assertEqual("[42]", self.lvide.__str__())
        self.lsingleton.inserer_position(1, 42)
        self.assertEqual("[1, 42]", self.lsingleton.__str__())


if __name__ == "__main__":
    unittest.main()
