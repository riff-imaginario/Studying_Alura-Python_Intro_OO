
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # Similar ao getter
    @property
    def nome(self):
        # title para primeira letra ser em maiusculo
        return self.__nome.title()

    # Similar ao setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome