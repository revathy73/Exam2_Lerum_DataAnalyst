class Avatar:

    def __init__(self):
        self.__stamina = 8
        self.__experience = 0

    @property
    def stamina(self) -> int:
        return self.__stamina

    @property
    def experience(self) -> int:
        return self.__experience

    def train(self):
        self.__stamina -= 1

    def rest(self):
        self.__stamina += 1

    def evolve(self):
        self.__experience += 1



