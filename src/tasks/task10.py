class Avatar:

    def __init__(self,stamina = 8,experience = 0) -> int:
        self.__stamina = stamina
        self.__experience = experience

    @property
    def train(self):
        self.__stamina -= 1

    @property
    def rest(self):
        self.__stamina += 1

    @property
    def evolve(self):
        self.__experience += 1

if __name__ == "__main__":

    value = Avatar(10,8)






