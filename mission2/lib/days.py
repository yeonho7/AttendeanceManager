from abc import ABC

class DayBase(ABC):
    point: int
    bonus_point: int
    bonus_threshold: int

class WednessDay(DayBase):
    point = 3
    bonus_point = 10
    bonus_threshold = 10

class Weekend(DayBase):
    point = 2
    bonus_point = 10
    bonus_threshold = 10

class Others(DayBase):
    point = 1
    bonus_point = 0
    bonus_threshold = 0




class Days:
    def __init__(self):
        self.attendance = {
            WednessDay : 0,
            Weekend : 0,
            Others : 0,
        }

    def attend(self, day_name):
        day = self.get_day(day_name)
        self.attendance[day] += 1

    @staticmethod
    def get_day(day_name):
        return {
            "wednesday": WednessDay,
            "saturday": Weekend,
            "sunday": Weekend,
        }.get(day_name, Others)
    def get_day_point(self):
        point = 0
        for day, cnt in self.attendance.items():
            point += day.point * cnt
            if cnt >= day.bonus_threshold:
                point += day.bonus_point
        return point

    @property
    def is_remove_condition(self):
        return self.attendance[WednessDay] == 0 and self.attendance[Weekend] == 0