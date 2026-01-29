class Avatar:

    def __init__(self,stamina,experience) -> int:
        self.__stamina = 8
        self.__experience = 0

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






