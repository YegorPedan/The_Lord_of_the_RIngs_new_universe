from units import Elf, Orc, Men, SuperMen, Dragon
from weapons import Bow, Sword, Knife, Baton
from teams import UnitsTeam
from help_functions import is_team_alive

if __name__ == "__main__":
    robin = Elf(1, 1, 1, Sword(1, 1, 1), 1)
    john = Men(5, 12, 44, Knife(5, 8, 7), 1, 2)
    team1 = UnitsTeam()
    team1.add_unit(robin)
    team1.add_unit(john)
    print("create a first team,", team1)

    # second team
    matrin = Elf(7, 4, 1, Bow(3, 1, 9), 2)
    jame = Orc(1, 5, 7, 2)
    team2 = UnitsTeam()
    team2.add_unit(matrin)
    team2.add_unit(jame)
    print("create a second team,", team2)

    # third team
    clark = SuperMen(1, 5, 7, Sword(1, 5, 7), 17, 1, 5)
    team3 = UnitsTeam()
    team3.add_unit(clark)
    print("create a third team,", team3)

    # fourth team
    smaug = Dragon(12, 17, 10)
    team4 = UnitsTeam()
    team4.add_unit(smaug)
    print("create a third team,", team4)
    print()

    team1.attack(team2)
    print("Team1 attack team2, ", f"{team2}")
    if team2.get_team_health() < 0:
        del team2

    team2.attack(team3)
    print("Team2 attack team3,", f"{team3}")
    if team3.get_team_health() < 0:
        del team3

    # team3.attack(team4)
    # print("Team3 attack team4,", f"{team4}")
    #
    # team4.attack(team1)
    # print("Team4 attack team1,", f"{team1}")
    #
    # team2.attack(team3)
    # print("Team2 attack team3", f"now team3 health is {team3}")
    # print()

    # print()
    # if is_team_alive(team1.get_team_health()):
    #     print("team 1 is alive")
    # if is_team_alive(team2.get_team_health()):
    #     print("team 2 is alive")
    # if is_team_alive(team3.get_team_health()):
    #     print("team 3 is alive")
    # if is_team_alive(team4.get_team_health()):
    #     print("team 4 is alive")
    # print("team2 has won")
