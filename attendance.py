id_map = {}
id_cnt = 0

# dat[사용자ID][요일]
attendance = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
wed = [0] * 100
weekend = [0] * 100

# day
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# grade
GOLD = 1
SILVER = 2
NORMAL = 0

def register_user(user_name) -> None:
    global id_cnt
    id_cnt += 1
    id_map[user_name] = id_cnt
    names[id_cnt] = user_name

def get_id(user_name):
    if user_name not in id_map:
        register_user(user_name)
    return id_map[user_name]


def get_index(day):
    index_map = {
        "monday" : MONDAY,
        "tuesday" : TUESDAY,
        "wednesday": WEDNESDAY,
        "thursday": THURSDAY,
        "friday": FRIDAY,
        "saturday": SATURDAY,
        "sunday": SUNDAY,
    }
    return index_map.get(day, None)

def is_wednesday(day_index):
    return day_index == WEDNESDAY

def is_weekend(day_index):
    return day_index in [SATURDAY, SUNDAY]

def get_day_point(day_index):
    if is_wednesday(day_index):
        return 3
    elif is_weekend(day_index):
        return 2
    return 1

def attend(user_name, day):
    user_id = get_id(user_name)
    day_index = get_index(day)
    if day_index is None:
        return

    attendance[user_id][day_index] += 1
    points[user_id] += get_day_point(day_index)
    if is_weekend(day_index):
        weekend[user_id] += 1

def parse_line(line):
    parts = line.strip().split()
    if len(parts) == 2:
        (user_name, day) = parts
        attend(user_name, day)

def build_attendance_data(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            for line in f.readlines():
                if not line:
                    break
                parse_line(line)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def get_bonus_point(user_id):
    point = 0
    if attendance[user_id][WEDNESDAY] > 9:
        point += 10
    if attendance[user_id][SATURDAY] + attendance[user_id][SUNDAY] > 9:
        point += 10
    return point

def get_grade(user_id):
    if points[user_id] >= 50:
        return GOLD
    if points[user_id] >= 30:
        return SILVER
    return NORMAL


def is_normal(user_id):
    return grade[user_id] not in (GOLD, SILVER)

def is_no_attend_on_wed_or_weekend(user_id):
    return wed[user_id] == 0 and weekend[user_id] == 0

def is_remove_condition(user_id):
    return is_normal(user_id) and is_no_attend_on_wed_or_weekend(user_id)

def determine_drop_out(file_path):
    build_attendance_data(file_path)

    for user_id in range(1, id_cnt + 1):
        points[user_id] += get_bonus_point(user_id)
        grade[user_id] = get_grade(user_id)

        print(f"NAME : {names[user_id]}, POINT : {points[user_id]}, GRADE : ", end="")
        if grade[user_id] == GOLD:
            print("GOLD")
        elif grade[user_id] == SILVER:
            print("SILVER")
        else:
            print("NORMAL")

    print("\nRemoved player")
    print("==============")
    for user_id in range(1, id_cnt + 1):
        if is_remove_condition(user_id):
            print(names[user_id])

if __name__ == "__main__":
    determine_drop_out("attendance_weekday_500.txt")