import socket
from threading import Thread
import pygame
import json

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping-pong")

fps = pygame.time.Clock()

# server connection
def server_connection():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect('localhost', 5555)
            id = int(client.recv(24).decode())
            buffer = ""
            return id, game_state, buffer, client
        except:
            pass
            print("Failed")

def receive():
    global buffer, game_state, game_over
    while not game_over:
        try:
            data = client.recv(1024).decode()
            buffer += data
            while '\n' in buffer:
                packed, buffer = buffer.split('\n', 1)
                if packed.strip():
                    game_state = json.loads(packed)

        except:
            game_state["winner"] = -1





id, game_state, buffer, client = server_connection()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    






    pygame.display.flip()
    fps.tick(60)