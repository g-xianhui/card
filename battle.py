#coding=utf-8

class Round(object):
    pass

class Battle(object):
    def __init__(self, avatar_list):
        assert(len(avatar_list) > 1)
        self.avatar_list = avatar_list
        self.history_rounds = []
        self.cur_round = None
        self.cur_turn = -1

    def on_battle_begin(self):
        for x in self.avatar_list:
            x.battle = self

    def on_battle_end(self):
        pass

    def is_end(self):
        l = [x for x in self.avatar_list if x.is_alive()]
        return len(l) <= 1

    def new_round(self):
        self.cur_round = Round()
        self.cur_turn = (self.cur_turn + 1) % len(self.avatar_list)

    def on_round_begin(self):
        for x in self.avatar_list:
            x.on_round_begin()

    def on_round_end(self):
        for x in self.avatar_list:
            x.on_round_end()
        self.history_rounds.insert(0, self.cur_round)

    def start(self):
        self.on_battle_begin()
        while not self.is_end():
            self.new_round()
            self.on_round_begin()
            action_player = self.avatar_list[self.cur_turn]
            action_player.action()
            self.on_round_end()
        self.on_battle_end()
