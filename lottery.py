#!/usr/bin/python
# -*- coding: UTF-8 -*-


class lottery:


    first = 0
    second = 0
    third = 0
    forth = 0
    fifth = 0
    sixth = 0
    welfare = 0
    lucky = False


    def match(self, pool, player, n) -> bool:
        global lucky
        lucky = False
        # check if lucky match
        if pool[6] == player[6]:
            n -= 1
            lucky = True
        # check if normal numbers match
        for num in player[:6]:
            if num in pool[:6]:
                n -= 1
            if n == 0:
                return True


    def win(self, pool, player) -> None:
        
        global first
        global second
        global third
        global forth
        global fifth
        global sixth
        global welfare

        if self.match(pool, player, 7):
            self.first += 1
            self.printStatus()
        elif self.match(pool, player, 6):
            if lucky is True:
                self.third += 1
                self.printStatus()
            else:
                self.second += 1
                self.printStatus()
        elif self.match(pool, player, 5):
            self.forth += 1
            self.printStatus()
        elif self.match(pool, player, 4):
            self.fifth += 1
        elif self.match(pool, player, 3):
            if lucky is True:
                self.sixth += 1
            else:
                self.welfare += 1
        elif self.match(pool, player, 2):
            if lucky is True:
                self.sixth += 1
            else:
                self.welfare += 1
        elif self.match(pool, player, 1):
            if lucky is True:
                self.sixth += 1
            else:
                self.welfare += 1
        else:
            self.welfare += 1

