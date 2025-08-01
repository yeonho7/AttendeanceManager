from lib.player import Player


class Roll:

    def __init__(self):
        self._players = {}

    def enroll(self, name):
        self._players[name] = Player(name)

    def is_enrolled(self, name):
        return name in self._players

    def get_player(self, name):
        return self._players[name]

    def attend(self, name, _day_name):
        if not self.is_enrolled(name):
            self.enroll(name)
        self.get_player(name).attend(_day_name)


    @property
    def players(self):
        return self._players.values()
    def print_players(self):
        for p in self.players:
            print(p)

    def print_drop_out(self):
        for p in self.players:
            if p.is_remove_condition:
                print(p.name)

