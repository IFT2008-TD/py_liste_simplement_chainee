from sequence import Sequence


class Element:
    """Classe accessoire pour la classe ListeSC. Représente une entrée de la liste."""
    def __init__(self, x):
        self.cle = x
        self.suivant = None


class ListeSC(Sequence):
    """
    Liste simplement chaînée. Les deux attributs sont :
        head (Element) : référence au premier Element
        cardinal (int) : nombre d'éléments stockés.

    Si la liste est vide, cardinal est 0, et head est None.

    Le premier élément de la liste est référé par head. Il est en position 0. Le dernier élément de la liste est celui
    dont le prochain est None. Il est en position cardinal-1.

    """

    def __init__(self, elements=None):
        """Construit une liste à partir d'un itérable.  Le premier élément de l'itérable sera référé par l'attribut head.
        
        Args :
            elements (iterable) : contient les éléments à insérer dans la liste
        """    
        if elements is None:
            elements = []
        self.head = None
        self.cardinal = 0
        for item in reversed(elements):
            self.inserer_premier(item)
        assert self._invariant()

    def __len__(self):
        """Retourne le nombre d'éléments dans la liste."""
        return self.cardinal

    def _compter_elements(self, item):
        """Compter récursivement les éléments de la liste. Utilié par l'invariant."""
        if item is None:
            return 0
        return 1 + self._compter_elements(item.suivant)

    def _invariant(self):
        """La liste est valide si, et seulement si, en comptant chaque élément de head à None on obtient le cardinal."""
        return self.cardinal == self._compter_elements(self.head)

    def _trouver_dernier(self, courant):
        """Trouve récursivement la référence au dernier élément de la liste (celui dont le suivant est None)
        Args :
            courant (Element) : Point de départ de la recherche récursive. Ne peut pas être None.
        Returns :
            Element : Référence au dernier élément de la liste. NB : La liste ne peut être vide!!!
            """
        if courant.suivant is None:
            return courant
        return self._trouver_dernier(courant.suivant)

    def _trouver_avant_dernier(self, courant):
        """Comme la méthode précédente mais avec l'avant-dernier élément. La liste doit avoir au-moins 2 éléments !"""
        if courant.suivant.suivant is None:
            return courant
        return self._trouver_avant_dernier(courant.suivant)

    def inserer_premier(self, x):
        """Ajoute la valeur x en première position de la liste."""
        item = Element(x)
        item.suivant = self.head
        self.head = item
        self.cardinal += 1
        assert self._invariant()

    def inserer_dernier(self, x):
        """Ajoute la valeur x en dernière position de la liste."""
        if self.head is None:
            self.inserer_premier(x)
        else:
            item = self._trouver_dernier(self.head)
            item.suivant = Element(x)
            self.cardinal += 1
            assert self._invariant()

    def retirer_premier(self):
        """Retire le premier élément de la liste. Retourne la valeur de l'élément retiré."""
        if self.head is None:
            return
        return_value = self.head.cle
        self.head = self.head.suivant
        self.cardinal -= 1
        assert self._invariant()
        return return_value

    def retirer_dernier(self):
        """Retire le dernier élément de la liste. Retourne la valeur de l'élément retiré."""
        if self.head is None:
            return
        if self.head.suivant is None:
            return self.retirer_premier()
        item = self._trouver_avant_dernier(self.head)
        return_value = item.suivant.cle
        item.suivant = None
        self.cardinal -= 1
        assert self._invariant()
        return return_value

    def _avancer(self, n, item):
        """Avance récursivement de n positions à partir de l'élément item."""
        if n == 0:
            return item
        return self._avancer(n - 1, item.suivant)

    def retirer_position(self, n):
        """Retire l'élément en position n. Retourne sa valeur. NB : Le premier élément a la position 0.
        NB : 0 <= n < cardinal sont les valeurs permises pour n."""
        assert 0 <= n < self.cardinal
        if n == self.cardinal - 1:
            return self.retirer_dernier()
        item = self._avancer(n, self.head)
        retval = item.cle
        item.cle = item.suivant.cle
        item.suivant = item.suivant.suivant
        self.cardinal -= 1
        assert self._invariant()
        return retval

    def inserer_position(self, n, x):
        """Insère un élément en position n, où 0 est le début de la liste. 0 <= n <= cardinal, de sorte qu'on peut 
        insérer en position 0 dans une liste vide, par exemple, où insérer en position 3 dans une liste comportant 
        3 éléments.
        """
        assert 0 <= n <= self.cardinal
        if n == self.cardinal:
            self.inserer_dernier(x)
            return
        item = self._avancer(n, self.head)
        ajout = Element(item.cle)
        item.cle = x
        ajout.suivant = item.suivant
        item.suivant = ajout
        self.cardinal += 1
        assert self._invariant()

    def inverse(self):
        """Retourne une liste inversée. Donc [1, 2, 3, 4] retournera [4, 3, 2, 1] !"""
        if self.head is None:
            return None
        inv = ListeSC()
        item = self.head
        while item is not None:
            inv.inserer_dernier(item.cle)

    def __str__(self):
        """Retourne une représentation textuelle de la liste."""
        return_value = "["
        item = self.head
        while item is not None:
            return_value += item.cle.__str__()
            if item.suivant is not None:
                return_value += ", "
            item = item.suivant
        return_value += "]"
        return return_value


if __name__ == "__main__":
    pass
