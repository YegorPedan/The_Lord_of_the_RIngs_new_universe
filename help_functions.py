
def is_number(input) -> bool:
    status = True
    try: 
        float(input)
    except:
        status = False
    return status
