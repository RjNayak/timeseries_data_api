
def is_number(val):
    return str(val).isnumeric()


def is_blank(val):
    result = False
    if not val:
        result = True
    return result


def is_valid_value(val):
    result = False
    if is_number(val) and type(val) is int:
        if val <= 180:
            result = True
    return result


def validate_input(val):
    result = False
    if is_number(val) and not is_blank(val) and is_valid_value(val):
        result = True
    return result
