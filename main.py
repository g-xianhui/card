#coding=utf-8

import battle
import avatar

if __name__ == '__main__':
    p1 = avatar.RobotAvatar('r1')
    p2 = avatar.RobotAvatar('r2')
    avatar_list = [p1, p2]
    battle = battle.Battle(avatar_list)
    battle.start()
