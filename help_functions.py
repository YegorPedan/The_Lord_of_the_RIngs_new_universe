
def is_number(input) -> bool:
    status = True
    try: 
        float(input)
    except:
        status = False
    return status

def is_team_alive(number) -> bool:
    is_alive = False 
    if number > 0:
        is_alive = True
    return is_alive
