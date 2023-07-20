from weapons import Bow, Baton, Sword, Knife


class Unit:
    def __init__(self, initial_health: int, speed: int, power: int):
        self._initial_health = initial_health
        self._speed = speed
        self._power = power

    def is_weapon_possible(self, weapon, available_weapons: tuple) -> bool:
        can_use = True 
        if not isinstance(weapon, available_weapons):
            can_use = False 
            print(f"Tha race {self.__class__.__name__} can not use a {weapon}")
        return can_use

    def get_health(self) -> int:
        return self._initial_health

    def __str__(self) -> str:
        return f"This unit is a {self.__class__.__name__} class"

class Elf(Unit):
    def __init__(self, initial_health: int, speed: int, power: int, weapon, possession_of_weapon: int):
        super().__init__(initial_health, speed, power)
        if self.is_weapon_possible(weapon, (Sword, Bow)):
            self.__weapon = weapon
            self.__possesion_of_weapon = possession_of_weapon
        else:
            self.__possesion_of_weapon = 0
            self.__weapon = None

    def get_total_force(self) -> float:
        power = 0
        if self.__weapon:
            power = (self._initial_health + self._speed * self._power + self.__possesion_of_weapon * self.__weapon.get_total_force()) / 100
        else:
            power = (self._initial_health + self._speed * self._power) / 100
        return power


class Orc(Unit):
    def __init__(self, initial_health: int, speed: int, power: int, number_of_rebirths: int):
        super().__init__(initial_health, speed, power)
        self.__number_of_rebirths = number_of_rebirths

    def get_total_force(self) -> float:
        return (self._initial_health + self._speed * self._power * self.__number_of_rebirths) / 100

class Men(Unit):
    def __init__(self, initial_health: int, speed: int, power: int, weapon, possession_of_weapon: int, intelligance: int):
        super().__init__(initial_health, speed, power)
        self._intelligance = intelligance
        if self.is_weapon_possible(weapon, (Sword, Bow, Knife)):
            self._weapon = weapon
            self._possesion_of_weapon = possession_of_weapon
        else:
            self._possesion_of_weapon = 0
            self._weapon = None

    def get_total_force(self) -> float:
        power = 0
        if self._weapon:
            power = (self._initial_health + self._speed * self._power + self._possesion_of_weapon * self._weapon.get_total_force()) / 100
        else:
            power = (self._initial_health + self._speed * self._power) / 100
        return power
            


class SuperMen(Men):
    def __init__(self, initial_health: int, speed: int, power: int, weapon, possession_of_weapon: int, intelligance: int, superpower: int):
        super().__init__(initial_health, speed, power, weapon, possession_of_weapon, intelligance)
        self.__superpower = superpower

    def get_total_force(self) -> float:
        power = 0
        if self._weapon:
            power = (self._initial_health + self._speed * self._power + self._possesion_of_weapon * self._weapon.get_total_force() ** self.__superpower) / 100
        else:
            power = (self._initial_health + self._speed * self._power ** self.__superpower) / 100
        return power

class Dragon(Unit):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_total_force(self):
        return self._initial_health * self._speed * self._power ** 5
