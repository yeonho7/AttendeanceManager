import pytest

from lib.player import Player
from lib.constants import *
from lib.grade import *

@pytest.fixture
def new_player():
    return Player("noname")

def test_uniq_player_id():
    a = Player("a")
    b = Player("b")
    c = Player("c")
    assert a.id == 1
    assert b.id == 2
    assert c.id == 3

def test_cal_point_monday(new_player):
    new_player.attend(MONDAY)
    assert new_player.point == 1

def test_cal_point_weekday_except_wed(new_player):
    new_player.attend(MONDAY)
    assert new_player.point == 1
    new_player.attend(TUESDAY)
    assert new_player.point == 2
    new_player.attend(THURSDAY)
    assert new_player.point == 3
    new_player.attend(FRIDAY)
    assert new_player.point == 4

def test_cal_point_wed(new_player):
    new_player.attend(WEDNESDAY)
    assert new_player.point == 3

def test_cal_point_weekend(new_player):
    new_player.attend(SATURDAY)
    assert new_player.point == 2
    new_player.attend(SUNDAY)
    assert new_player.point == 4

def test_no_bonus_point(new_player):
    for i in range(10):
        new_player.attend(MONDAY)
    assert new_player.point == 10
def test_wed_bonus_point(new_player):
    for i in range(10):
        new_player.attend(WEDNESDAY)
    assert new_player.point == (3 * 10 + 10)

def test_weekend_bonus_point(new_player):
    for i in range(5):
        new_player.attend(SATURDAY)
        new_player.attend(SUNDAY)
    assert new_player.point == (2 * 10 + 10)

def test_gold_grade(new_player):
    for i in range(10):
        new_player.attend(WEDNESDAY) # 3 * 10 + 10
        new_player.attend(MONDAY) # 1 * 10
    assert new_player.grade == Gold


def test_silver_grade(new_player):
    for i in range(30):
        new_player.attend(MONDAY)
    assert  new_player.grade == Silver

def test_normal_grade(new_player):
    assert new_player.grade == Normal
    for i in range(10):
        new_player.attend(MONDAY)
    assert new_player.grade == Normal

def test_remove_condition_at_first(new_player):
    assert new_player.is_remove_condition

@pytest.mark.parametrize("day", [MONDAY, TUESDAY, THURSDAY, MONDAY])
def test_remove_condition_with_attendance(new_player, day):
    new_player.attend(day)
    assert new_player.is_remove_condition

@pytest.mark.parametrize("day", [WEDNESDAY, SATURDAY, SUNDAY])
def test_no_remove_condition_because_wed(new_player, day):
    new_player.attend(day)
    assert new_player.is_remove_condition == False

def test_no_remove_condition_because_grade(new_player):
    for _ in range(30):
        new_player.attend(MONDAY)
    assert new_player.is_remove_condition == False


def test_player_print(new_player):
    new_player.attend(WEDNESDAY)
    assert str(new_player) == "NAME : noname, POINT : 3, GRADE : NORMAL"