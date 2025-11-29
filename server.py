import socket
import json
import threading
import time
import random

WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7

class GameServer:
    def __init__(self, host='localhost', port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print("Server started")
        
        self.clients = {0: None, 1: None}
        self.connected = {0: False, 1: False}

    def run(self):
        while True:
            self.accept_players()
            self.reset_game_state()
            threading.Thread(target=self.ball, daemon=True).start()

            while not self.game_over and all(self.connected.values()):
                time.sleep(0.1)
            
            print("Player wins")
            time.sleep(3)

            for p_id in [0, 1]:
                try:
                    self.clients[p_id].close()
                except:
                    pass

