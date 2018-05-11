def basic_check(func):
    def check_sides(sides):
        # Check for malicous input and return True if found
        if len(sides) != 3:
            raise ValueError("Definately not a triangle")
        if ((sides[0] < 0) or (sides[1] < 0) or (sides[2] < 0)):
            raise ValueError("Degenerate Triangles not allowed")
        if ((sides[0] == 0) or (sides[1] == 0) or (sides[2] == 0)):
            return False
        sides = sorted(sides)
        if (sides[0] + sides[1]) < sides[2]:
            return False
        return func(sides)
    return check_sides


@basic_check
def is_equilateral(sides):
    if (sides[0] == sides[1]) and (sides[0] == sides[2]):
        return True
    return False


@basic_check
def is_isosceles(sides):
    # No need to check s[0] with s[2] since sides is sorted
    if (sides[0] == sides[1]) or (sides[1] == sides[2]):
        return True
    return False


@basic_check
def is_scalene(sides):
    # No need to check s[0] with s[2] since sides is sorted
    if (sides[0] != sides[1]) and (sides[1] != sides[2]):
        return True
    return False
