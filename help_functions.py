
def is_number(input) -> bool:
    status = True
    try:
        float(input)
    except ValueError:
        status = False
    return status


def is_team_alive(team) -> bool:
    return team.get_team_health() != 0


# just for tast an idea
# def is_team_alive(team) -> bool:
#     status = True
#     try:
#         team.get_team_health()
#     except NameError:
#         status = False
#     return status


# can not be implemented in python
# need to check that object exists before passing to function
# def team_attack(attacking, attacked):
#     if not is_team_alive(attacking):
#         print(f"{attacking} team already dead")
#     elif not is_team_alive(attacked):
#         (f"{attacked} already dead")
#     else:
#         attacking.attack(attacked)
#         print(
#             f"{attacking} successfully attacked {attacked}, now {attacked} health is {attacked.get_team_health()}")
