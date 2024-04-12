import pygame

from player import Player, RED_PLAYER, BLUE_PLAYER

RED_PLAYER = 0
BLUE_PLAYER = 1

class Player:
  def __init__(self, position, id):
    self.__position = position
    self.__id = id
    self.__direction_heading = 0
  
  def get_id(self):
    return self.__id


def main():
  
  red_player = Player([10, 10], RED_PLAYER)
  blue_player = Player([30, 10], BLUE_PLAYER)
  
  
main()