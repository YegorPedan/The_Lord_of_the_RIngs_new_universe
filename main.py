from units import Elf, Orc, Men, SuperMen, Dragon
from weapons import Bow, Sword, Knife, Baton
from teams import UnitsTeam

if __name__ == "__main__":
    robin = Elf(1, 1, 1, Sword(1, 1, 1), 1)
    john = Men(5, 12, 44, Knife(5, 8, 7), 1, 2)
    team1 = UnitsTeam()
    team1.add_unit(robin)
    team1.add_unit(john)
    print("create a first team,", team1)
   
    #second team
    matrin = Elf(7, 4, 1, Bow(3, 1, 9), 2)
    jame = Orc(1, 5, 7, 2)
    team2 = UnitsTeam()
    team2.add_unit(matrin)
    team2.add_unit(jame)
    print("create a second team,", team2)

    #third team
    clark = SuperMen(1, 5, 7, Sword(1, 5, 7), 17, 1, 5)
    team3 = UnitsTeam()
    team3.add_unit(clark)
    print("create a third team,", team3)

    #fourth team
    smaug = Dragon(1, 17, 8)
    team4 = UnitsTeam()
    team4.add_unit(smaug)
    print("create a third team,", team4)
