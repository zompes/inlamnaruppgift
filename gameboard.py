from random import random
from Player import Player

class GameBoard:
    spelar_lista = []
    # constructor
    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        # create four different objects
        self.red_cube = Player('red',self,'cube', 50)
        self.red_triangle = Player('red', self,'triangle', 30)
        self.blue_triangle = Player('blue', self,'triangle', 30)
        self.blue_cube = Player('blue',self,'cube', 50)
        self.spelar_lista.append(self.red_cube)
        self.spelar_lista.append(self.red_triangle)
        self.spelar_lista.append(self.blue_cube)
        self.spelar_lista.append(self.blue_triangle)

    # use __str__ to create a html representation
    def __str__(self):
        return f"""
            <div class="spel-plan" id="{self.id}">
                {self.red_triangle}
                {self.red_cube}
                {self.blue_cube}
                {self.blue_triangle}
            </div>
            <div class="player-name"></div>
        """