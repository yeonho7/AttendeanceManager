from lib.days import Days
from lib.grade import get_grade

class Player:
    _id_cnt = 0
    def __init__(self, name):
        self.name = name
        self.id = self.get_new_id()
        self._point = 0
        self.days = Days()

    @classmethod
    def get_new_id(cls):
        cls._id_cnt += 1
        return cls._id_cnt

    def __str__(self):
        return(f"NAME : {self.name}, POINT : {self.point}, GRADE : {self.grade.name}")

    def attend(self, day_name: str):
        self.days.attend(day_name)

    @property
    def point(self) -> int:
        return self.days.get_day_point()

    @property
    def grade(self):
        return get_grade(self.point)

    @property
    def is_remove_condition(self):
        return self.days.is_remove_condition and self.grade.is_remove_condition
