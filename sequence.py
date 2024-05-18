class Sequence:
    def inserer_premier(self, x):
        raise NotImplementedError

    def inserer_dernier(self, x):
        raise NotImplementedError

    def retirer_premier(self):
        raise NotImplementedError

    def retirer_dernier(self):
        raise NotImplementedError

class SequenceError(Exception):
    pass

class SequenceVideError(SequenceError):
    pass