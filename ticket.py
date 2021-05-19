#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import sys

sys.path

class ticket(object):


    def genTicket(luckyNum) -> list:

        ticket = []
        
        num1 = random.randint(1, 33)

        ticket.append(num1)

        # i = 1
        def numGen(num2) :
            # global rep
            while num2 in ticket:

                num2 = random.randint(1, 33)

            ticket.append(num2)

        
        for i in range(5):
            num2 = random.randint(1, 33)
            numGen(num2)

        ticket.sort()
        ticket.append(luckyNum)
        return ticket
    
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


class control:
    
    def gen1(lucky, luckyNum, diy, numList) -> list:
        if lucky and diy:
            raise ValueError("it can't be luck and diy")
        
        if lucky :
            tk = ticket.genTicket(luckyNum)
        elif diy :
            if len(numList) != 7:
                raise ValueError("the length of a ticket has to be 7")
            tk = numList
        else :
            tk = ticket.genTicket(random.randint(1, 16))
        return tk


    def genN(n, lucky, luckyNum, diy, numList) -> list:
    
        tickets = []

        for i in range(n):
            tickets.append(control.gen1(lucky, luckyNum, diy, numList))

        return tickets

if __name__ == '__main__':
    print(control.genN(10, False,0,False,[0]))