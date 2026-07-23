#imports
import numpy as np

#TMP RULES
'''
we have a grid (28x28 ? could be a good start, maybe more)
every cell of the grid has two states: 
    - alive
    - dead
if live cell has:
    - less then two live cells adjacent it dies
    - 2-3 live cells adjacent it lives
    - more then 3 adjecent cells it dies
if a dead cell has:
    - exactly 2 live cells adjacent it borns (becomes alive)
'''


#classes
'''
need to define a cell class that at every tick it checks the surrounding neighbors state
i guess there are technically three (?, maybe two) possible states: 
    - alive
    - dead
    - bound (count as dead (?))
'''
# class Cell:
#     """
#     this is the cell class
#     """  
#     def determine_neighbors(pos, border):
#         x, y = pos
        
    
#     def __init__(self, pos, border, alive):
#         self.state = alive
        
#         self.neighbors = 

    

#     def check_neighbors():
#         x, y = self.pos
#         alive_neighbors = 0

#         neighbors = []

#     def change_state():
        #function that determines the state at the next iteration

    #maybe a position attribute ???

    #maybe an attribute to determine whether its a bound cell or not ???

    #maybe just have functions that determine the state of the neighbors and 
    #change the state based on the count of neighbors
        

'''
I need to also define a grid class (?)
not sure about this one, maybe I can manage to do it without recurring to class objects
'''
'''
again, I don't know yet, but an idea could be to create an object grid that takes as 
an input a map(matrix) and creates a grid with cells following the map, and said grid
could have a method "run" that takes as an input the number of iteration and run the 
cells inside for said amount
'''
class Grid:
    def __init__(self, inparr):
        self.shape = inparr.shape
        self.current_state = inparr
        self.next_state = np.zeros_like(inparr)
        self.num_nghbr_state = np.zeros_like(inparr)


    def check_nghbrs(self, i):
        x, y = i
        num_alive = 0
        for r in range(x-1, x+2):
            for c in range(y-1, y+2):
                try:
                    if self.current_state[r][c] == 1 and (r, c) != (x, y) and (r >= 0) and (c >= 0) :
                        num_alive += 1
                except IndexError:
                    pass
                # print(i, '->', (r, c), 'current num alive:', num_alive) #useful for debugging

        return num_alive
    
    def update_stage(self, itr = 1):
        print(self.current_state)
        for it in range(itr):
            for x in range(self.shape[0]):
                for y in range(self.shape[1]):
                    pnt_stt = self.current_state[x][y]
                    pos = (x, y)
                    alive_nghbr = self.check_nghbrs(pos)
                    self.num_nghbr_state[x][y] = alive_nghbr

                    #update block
                    match pnt_stt:
                        case 1:
                            if (alive_nghbr < 2) or (alive_nghbr > 3):
                                self.next_state[x][y] = 0
                            else:
                                self.next_state[x][y] = 1
                        case 0:
                            if alive_nghbr == 3:
                                self.next_state[x][y] = 1
                            else:
                                self.next_state[x][y] = 0

            # print(self.num_nghbr_state) #useful for debugging
            print(self.next_state)
            self.current_state = np.copy(self.next_state)
        return self.current_state
        