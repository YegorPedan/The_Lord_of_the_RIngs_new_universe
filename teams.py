from units import Unit
from help_functions import is_number

from user_exceptions import AttackTypeError, TeamTypeError


class UnitsTeam:
    def __init__(self) -> None:
        self.units = []
        self.__team_health = 0

    def __add_unit(self, unit) -> None:
        if (isinstance(unit, Unit)):
            self.units.append(unit)
            self.__team_health += unit._initial_health
        else:
            raise TeamTypeError("Only units can be added to a team")

    def add_unit(self, unit) -> None:
        try:
            self.__add_unit(unit)
        except TeamTypeError:
            print("Please choose another character!")

    def __reduce_common_health(self, number: float) -> None:
        if is_number(number):
            self.__team_health -= number
            self.__team_health = 0 if self.__team_health < 0 else self.__team_health
        else:
            raise AttackTypeError("Attack can be only a float number")

    def attack(self, attacked_team: "UnitsTeam") -> bool:
        can_be_attacked = True
        if attacked_team.__team_health <= 0:
            print("That team already destroyed")
            can_be_attacked = False
        else:
            common_power = 0
            for unit in self.units:
                common_power += unit.get_total_force()
            try:
                attacked_team.__reduce_common_health(common_power)
            except AttackTypeError:
                print("Please pass a float number to attack method")
        return can_be_attacked

    def get_team_health(self) -> float:
        return self.__team_health

    def __str__(self) -> str:
        return f"current team health is {self.__team_health}"
