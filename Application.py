from random import random
from browser import window
j = window.jQuery
from network_brython import connect, send, close
from SpelPlan import SpelPlan

# INTE KLART, SAKNAR ÅTMINSTONE SPELARLOOPEN OCH NÄTVERK

class Application:

    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]

        def network_events(timestamp, user_name, message):
            print(f"{timestamp} {user_name} {message}")
            if user_name == 'system' and 'created the channel' in message:
                self.red_player_name = message.split("'")[1]
                self.current_player_name = self.red_player_name
                print(f'Red player {self.red_player_name}')
            if user_name == 'system' and  'joined channel' in message:
                name = message.split(' ')[1]
                if name != self.red_player_name:
                    self.blue_player_name = name 
                    print(f'Blue player {self.blue_player_name}')
                    self.start_game_loop()
        
        name = input("Ditt namn:")
        channel = input("Skapa eller anslut till kanal (ange kanalnamn)")
        connect(channel, name, network_events)

        self.spel_plan = SpelPlan()

    def start_game_loop():
        print( j('.player-name').length)
        j('.player-name').html(f'{current_player_name}s tur')


 

    def __str__(self):
        return f"""
            <div class="application" id={self.id}>
              {''.join(str(self.spel_plan))}
            </div>
        """
