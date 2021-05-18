import ticket
import lottery as lt


# TODO: coming soon
class level :

    def __init__(self, lv) -> None:
        super().__init__()




class control:
    
    def gen1(self, lucky, luckyNum, diy, numList) -> ticket:
        if lucky and diy:
            raise ValueError("it can't be luck and diy")
        
        if lucky :
            tk = ticket(luckyNum)
        elif diy :
            if len(numList) != 7:
                raise ValueError("the length of a ticket has to be 7")
            tk = ticket(numList)

        return tk


    def genN(self, n, lucky, luckyNum, diy, numList) -> list:
    
        tickets = []

        for i in range(n):
            tickets.append(self.gen1(lucky, luckyNum, diy, numList))

        return tickets
    


    