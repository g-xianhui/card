#coding=utf-8

class Avatar(object):
    def __init__(self):
        self.battle = None
        self.round = None
        self.target = None
        self.skill = None
        self.hp = 0
        self.mp = 0
        self.buff_list = []
        self.equip_list = []
        self.library = None
        self.hand_cards = {}
        self.hand_limit = 0
        self.draw_number = 0

    def build_library(self):
        pass

    def draw_card(self):
        if not self.library:
            self.build_library()
        card_id = self.library.pop()
        card = Card(card_id)
        self.hand_cards[card.uid] = card

    def drop_card(self, card_uid):
        self.hand_cards.pop(card_uid, None)

    def use_card(self, card_uid):
        card = self.hand_cards.get(card_uid)
        if card:
            if card.check_trigger(self):
                self.hand_cards.pop(card_uid, None)
                card.trigger(self)
            else:
                pass
        else:
            pass

    def add_buff(self, buff):
        pass

    def use_skill(self, skill_id):
        pass

    def turn(self):
        pass

    def turn_begin(self):
        pass

    def turn_end(self):
        pass

    def add_hp(self, n):
        pass

    def add_mp(self, n):
        pass

    def dead(self):
        pass
