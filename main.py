from src.ship_input import input_ships
from src.bot_generation import bot_ships
from src.gameplay import game
import os

os.makedirs("data",exist_ok=True)

input_ships()
bot_ships()
game()
