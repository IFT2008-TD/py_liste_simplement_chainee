"""
Exercice bonus :
--------------

Une fois que vous avez complété les primitives de votre liste simplement chaînée à votre goût, écrivez une fonction qui
prend une liste contenant 2n éléments, et renverse la deuxième moitié.  Donc la liste suivante :
[1, 2, 3, 4, 5, 6, 7, 8] devient [1, 2, 3, 4, 8, 7, 6, 5]...

Estimez la complexité de votre algorithme. Estimez aussi la complexité des primitives de la liste
"""


def renverser_moitie(l):
    """Prend une liste l contenant 2n élément et inverse l'ordre des n derniers éléments."""
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maListe = [1, 2, 3, 4, 5, 6, 7, 8]
    renverser_moitie(maListe)
    print("Attendu : [1, 2, 3, 4, 8, 7, 6, 5]")
    print(f"Obtenu  : {maListe}")

