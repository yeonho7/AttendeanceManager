from abc import ABC


class Grade(ABC):
    name: str
    threshold: int
    is_remove_condition: bool

class Gold(Grade):
    name = "GOLD"
    threshold = 50
    is_remove_condition = False

class Silver(Grade):
    name = "SILVER"
    threshold = 30
    is_remove_condition = False

class Normal(Grade):
    name = "NORMAL"
    threshold = 0
    is_remove_condition = True


def get_grade(point):
    if point >= Gold.threshold:
        return Gold
    if point >= Silver.threshold:
        return Silver
    return Normal
