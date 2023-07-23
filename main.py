from units import Elf, Orc, Men, SuperMen, Dragon
from weapons import Bow, Sword, Knife, Baton
from teams import UnitsTeam
from help_functions import is_team_alive

if __name__ == "__main__":
    robin = Elf(1, 1, 1, Sword(1, 1, 1), 1)
    john = Men(5, 12, 44, Knife(5, 8, 7), 1, 2)
    team1 = UnitsTeam("team1")
    team1.add_unit(robin)
    team1.add_unit(john)
    print("create a first team,", team1)

    # second team
    matrin = Elf(7, 4, 1, Bow(3, 1, 9), 2)
    jame = Orc(1, 5, 7, 2)
    team2 = UnitsTeam("team2")
    team2.add_unit(matrin)
    team2.add_unit(jame)
    print("create a second team,", team2)

    # third team
    clark = SuperMen(1, 5, 7, Sword(1, 5, 7), 17, 1, 5)
    team3 = UnitsTeam("team3")
    team3.add_unit(clark)
    print("create a third team,", team3)

    # fourth team
    smaug = Dragon(12, 17, 10)
    team4 = UnitsTeam("team4")
    team4.add_unit(smaug)
    print("create a fourth team,", team4)
    print()

    # use garbage collector
    all_teams = [team1, team2, team3, team4]
    for team_index in range(len(all_teams)):
        attacker = all_teams[team_index % len(all_teams)]
        victim = all_teams[(team_index + 1) % len(all_teams)]
        print(f"{attacker} attack {victim}")
        attacker.attack(victim)
        print(f"after attack {victim} health is {victim.get_team_health()}")
        if not is_team_alive(victim):
            print(f"{victim} was deleted from battlefield!")
            all_teams.remove(victim)

    # use del function
    # team1.attack(team2)
    # if team2.get_team_health() == 0:
    #     del team2
    #
    # try:
    #     team2.attack(team3)
    #     if team3.get_team_health() == 0:
    #         del team3
    # except NameError:
    #     print("team3 already removed")
    #
    # try:
    #     team3.attack(team4)
    #     if team4.get_team_health() == 0:
    #         del team4
    # except NameError:
    #     print("team2 already removed")
    #
    # try:
    #     team4.attack(team1)
    #     if team1.get_team_health() == 0:
    #         del team1
    # except NameError:
    #     print("team4 already removed")
