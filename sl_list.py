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
        pass

    def __len__(self):
        """Retourne le nombre d'éléments dans la liste."""
        pass

    def _compter_elements(self, item):
        """Compter récursivement les éléments de la liste. Utilié par l'invariant."""
        pass

    def _invariant(self):
        """La liste est valide si, et seulement si, en comptant chaque élément de head à None on obtient le cardinal."""
        pass

    def _trouver_dernier(self, courant):
        """Trouve récursivement la référence au dernier élément de la liste (celui dont le suivant est None)
        Args :
            courant (Element) : Point de départ de la recherche récursive. Ne peut pas être None.
        Returns :
            Element : Référence au dernier élément de la liste. NB : La liste ne peut être vide!!!
            """
        pass

    def _trouver_avant_dernier(self, courant):
        """Comme la méthode précédente mais avec l'avant-dernier élément. La liste doit avoir au-moins 2 éléments !"""
        pass

    def inserer_premier(self, x):
        """Ajoute la valeur x en première position de la liste."""
        pass

    def inserer_dernier(self, x):
        """Ajoute la valeur x en dernière position de la liste."""
        pass

    def retirer_premier(self):
        """Retire le premier élément de la liste. Retourne la valeur de l'élément retiré."""
        pass

    def retirer_dernier(self):
        """Retire le dernier élément de la liste. Retourne la valeur de l'élément retiré."""
        pass

    def _avancer(self, n, item):
        """Avance récursivement de n positions à partir de l'élément item."""
        pass

    def retirer_position(self, n):
        """Retire l'élément en position n. Retourne sa valeur. NB : Le premier élément a la position 0.
        NB : 0 <= n < cardinal sont les valeurs permises pour n."""
        pass

    def inserer_position(self, n, x):
        """Insère un élément en position n, où 0 est le début de la liste. 0 <= n <= cardinal, de sorte qu'on peut 
        insérer en position 0 dans une liste vide, par exemple, où insérer en position 3 dans une liste comportant 
        3 éléments.
        """
        pass

    def inverse(self):
        """Retourne une liste inversée. Donc [1, 2, 3, 4] retournera [4, 3, 2, 1] !"""
        pass

    def __str__(self):
        """Retourne une représentation textuelle de la liste."""
        pass


if __name__ == "__main__":
    pass
