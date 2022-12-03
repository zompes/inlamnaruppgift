import random
from browser import window
j = window.jQuery
from network_brython import connect, send, close
from gameboard import GameBoard

# INTE KLART, SAKNAR ÅTMINSTONE SPELARLOOPEN OCH NÄTVERK

class Application:

    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random.random()).split('.')[1]
        
        username = input("Ditt namn:")
        channel = input("Skapa eller anslut till kanal (ange kanalnamn)")
        connect(channel, username, self.loop)
        self.spel_plan = GameBoard()

    def loop(self, timestamp, user_name, message):
        print(f"timestamp={timestamp}, username={user_name}, message={message}")

        if user_name == 'system' and 'created the channel' in message:
            self.red_player_name = message.split("'")[1]
            self.current_player_name = self.red_player_name
            print(f'Red player {self.red_player_name}')
        elif user_name == 'system' and  'joined channel' in message:
            name = message.split(' ')[1]
            if name != self.red_player_name:
                self.blue_player_name = name 
                print(f'Blue player {self.blue_player_name}')
                # self.start_game_loop()
        else:
            # Game loop
            self.handle_event(message)
    
    def handle_event(self, data):
        print(f"{self.my_color} received event")

        event_type = data.get("type")
        if event_type == "ATTACK":
            attacker_color = data["attacker"]
            print("Ohh noo, some was attacked!")
        else:
            print(f"Boring... {event_type}")

    def start_game_loop(self):
        print("Starting game loop")
        print(f"Player names: red={self.red_player_name}, blue={self.blue_player_name}")

        print(j('.player-name').length)
        j('.player-name').html(f'{self.current_player_name}s tur')

    def __str__(self):
        return f"""
            <div class="application" id={self.id}>
              {''.join(str(self.spel_plan))}
            </div>
        """
