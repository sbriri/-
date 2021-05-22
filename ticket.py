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
    count = 0
    lucky = False


    def match(pool, player, n) -> bool:
        lottery.lucky = False
        # check if lucky match
        if pool[6] == player[6]:
            n -= 1
            lottery.lucky = True
        # check if normal numbers match
        for num in player[:6]:
            if num in pool[:6]:
                n -= 1
            if n == 0:
                return True


    def win(pool, player) -> None:
        
        lottery.count += 1
        if lottery.match(pool, player, 7):
            lottery.first += 1
            lottery.printStatus()
        elif lottery.match(pool, player, 6):
            if lottery.lucky is True:
                lottery.third += 1
                lottery.printStatus()
            else:
                lottery.second += 1
                lottery.printStatus()
        elif lottery.match(pool, player, 5):
            lottery.forth += 1
            lottery.printStatus()
        elif lottery.match(pool, player, 4):
            lottery.fifth += 1
        elif lottery.match(pool, player, 3):
            if lottery.lucky is True:
                lottery.sixth += 1
            else:
                lottery.welfare += 1
        elif lottery.match(pool, player, 2):
            if lottery.lucky is True:
                lottery.sixth += 1
            else:
                lottery.welfare += 1
        elif lottery.match(pool, player, 1):
            if lottery.lucky is True:
                lottery.sixth += 1
            else:
                lottery.welfare += 1
        else:
            lottery.welfare += 1



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
    lot = control.gen1(False,0,False,[0])
        
    tkts = control.genN(10,False,0,False,[0])

    for tkt in tkts:
        lottery.win(lot,tkt)

    print("first " + str(lottery.first))
    print("second " + str(lottery.second))
    print("third " + str(lottery.third))
    print("forth " + str(lottery.forth))
    print("fifth " + str(lottery.fifth))
    print("sixth " + str(lottery.sixth))
    print("welfare " + str(lottery.welfare))
    print("count " + str(lottery.count))
    print("===========================")
    print("get  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥")
    print("spend " + str(lottery.count * 2))