#coding=utf-8

class Battle(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.history_rounds = []
        self.cur_round = None

    def start(self):
        while True:
            self.cur_round = self.new_round(self.cur_round)
            attacker = self.cur_round.attacker
            defencer = self.cur_round.defencer
            attacker.attack()
            if attacker.dead():
                pass
            elif defencer.dead():
                pass
            elif attacker.exit():
                pass
            elif defencer.exit():
                pass
            else:
                pass
