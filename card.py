#coding=utf-8

import global_data
import card_data

class Card(object):
    def __init__(self, cid):
        self.id = cid
        self.uid = global_data.get_uid()
        self.info = card_data.get(cid)

    def check_trigger(self, owner):
        pass

    def trigger(self, owner):
        pass
