#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import sys

sys.path

class ticket(object):
    
    def __init__(self, luckyNum) -> None:
        self = self.genTicket(luckyNum)


    def __init__(self, numList) -> None:
        self = numList

    def genTicket(self, luckyNum) -> list:

        ticket = []
        
        num1 = random.randint(1, 33)

        ticket.append(num1)

        # i = 1
        def numGen(self, num2) :
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

