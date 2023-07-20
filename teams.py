from units import Unit
from help_functions import is_number 

class UnitsTeam:
    def __init__(self) -> None:
        self.units = []
        self.__team_health = 0

    def add_unit(self, unit) -> None:
        if (isinstance(unit, Unit)):
            self.units.append(unit)
            self.__team_health += unit._initial_health
        else:
            raise ValueError("Only units can be added to team")

    def __reduce_common_health(self, number: float) -> None:
        if is_number(number):
            self.__team_health -= number
        else:
            raise TypeError("")

    def team_attack(self, attacked_team: "UnitsTeam") -> bool:
        can_be_attacked = True
        if attacked_team.__team_health <= 0:
            print("That team already destroyed")
            can_be_attacked = False
        else:
            common_power = 0
            for unit in self.units:
                common_power += unit.get_power()
            attacked_team.__reduce_common_health(common_power)
        return can_be_attacked

    def __str__(self) -> str:
        return f"current team health is {self.__team_health}"
