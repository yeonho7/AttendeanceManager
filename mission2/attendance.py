from lib.roll import Roll


def parse_line(line):
    parts = line.strip().split()
    if len(parts) == 2:
        return parts
    return None

def read_file(file_path):
    lines = []
    try:
        with open(file_path, encoding='utf-8') as f:
            for line in f.readlines():
                parts = parse_line(line)
                if parts is not None:
                    lines.append( parts )
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    return lines

def load_attendance_data(file_path) -> Roll:
    roll = Roll()
    lines = read_file(file_path)
    for player_name, day in lines:
        roll.attend(player_name, day)
    return roll

def determine_drop_out(file_path):
    roll = load_attendance_data(file_path)
    roll.print_players()
    print("\nRemoved player")
    print("==============")
    roll.print_drop_out()

if __name__ == "__main__":
    determine_drop_out("attendance_weekday_500.txt")