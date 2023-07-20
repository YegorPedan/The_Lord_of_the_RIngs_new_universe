class Weapon:
    def __init__(self, impact_force: int, breaking_capacity: int):
        self._impact_force = impact_force
        self._breaking_capacity = breaking_capacity

    def __str__(self) -> str:
        return self.__class__.__name__


class Bow(Weapon):
    def __init__(self, impact_force: int, breaking_capacity: int, range: int):
        super().__init__(impact_force, breaking_capacity)
        self.__range = range

    def get_total_force(self) -> int:
        return self._impact_force * self._breaking_capacity + self.__range


class Sword(Weapon):
    def __init__(self, impact_force: int, breaking_capacity: int, endurance: int):
        super().__init__(impact_force, breaking_capacity)
        self.__endurance = endurance

    def get_total_force(self) -> int:
        return self._impact_force * self._breaking_capacity + self.__endurance


class Knife(Weapon):
    def __init__(self, impact_force: int, breaking_capacity: int, endurance: int):
        super().__init__(impact_force, breaking_capacity)
        self.__endurance = endurance

    def get_total_force(self) -> int:
        return self._impact_force * self._breaking_capacity + self.__endurance


class Baton(Weapon):
    def __init__(self, impact_force: int, breaking_capacity: int, endurance: int):
        super().__init__(impact_force, breaking_capacity)
        self.__endurance = endurance

    def get_total_force(self) -> int:
        return self._impact_force * self._breaking_capacity + self.__endurance

