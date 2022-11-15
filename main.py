# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
  print("INFO")

  return {
    "apiversion": "1",
    "author": "Titan0932",  # TODO: Your Battlesnake Username
    "color": "#273469",  # TODO: Choose color
    "head": "all-seeing",  # TODO: Choose head
    "tail": "mlh-gene",  # TODO: Choose tail
  }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
  print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
  print("GAME OVER\n")


def checkIfBodyPartsInCornerDangerZone(myBody, coordinateAxis, value):
  for bodyPart in myBody:
    if bodyPart[coordinateAxis] == value:
      return True
  return False


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

  is_move_safe = {"up": True, "down": True, "left": True, "right": True}

  # We've included code to prevent your Battlesnake from moving backwards
  my_head = game_state["you"]["body"][0]  # Coordinates of your head
  my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"

  if my_neck["x"] < my_head["x"]:  # Neck is left of head, don't move left
    is_move_safe["left"] = False

  elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
    is_move_safe["right"] = False

  elif my_neck["y"] < my_head["y"]:  # Neck is below head, don't move down
    is_move_safe["down"] = False

  elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
    is_move_safe["up"] = False

  # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
  board_width = game_state['board']['width']
  board_height = game_state['board']['height']
  if my_head["x"] == 0:
    is_move_safe["left"] = False
  elif my_head["x"] >= board_width - 1:
    is_move_safe["right"] = False

  if my_head["y"] == 0:
    is_move_safe["down"] = False
  elif my_head["y"] >= board_height - 1:
    is_move_safe["up"] = False

  # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
  my_body = game_state['you']['body']
  for bodyCoordinates in my_body:
    if my_head["x"] - 1 == bodyCoordinates["x"] and my_head[
        "y"] == bodyCoordinates["y"]:
      is_move_safe["left"] = False
    elif my_head["x"] + 1 == bodyCoordinates["x"] and my_head[
        "y"] == bodyCoordinates["y"]:
      is_move_safe["right"] = False

    if my_head["y"] - 1 == bodyCoordinates["y"] and my_head[
        "x"] == bodyCoordinates["x"]:
      is_move_safe["down"] = False
    elif my_head["y"] + 1 == bodyCoordinates["y"] and my_head[
        "x"] == bodyCoordinates["x"]:
      is_move_safe["up"] = False

  #Prevent the snake from going into the corner if there's no way out
  mySnakeLength = len(game_state['you']['body'])
  # For top-left
  if my_head["x"] != mySnakeLength - 1 and my_head["y"] == game_state['board'][
      'height'] - 1 and checkIfBodyPartsInCornerDangerZone(
        game_state['you']['body'], 'x', 0):
    is_move_safe["left"] = False
  elif my_head[
      "y"] != game_state['board']['height'] - mySnakeLength and my_head[
        "x"] == 0 and checkIfBodyPartsInCornerDangerZone(
          game_state['you']['body'], 'y', game_state['board']['height'] - 1):
    is_move_safe["up"] = False

    # For top-right
  if my_head["x"] != game_state['board']['width'] - mySnakeLength and my_head[
      "y"] == game_state['board'][
        'height'] - 1 and checkIfBodyPartsInCornerDangerZone(
          game_state['you']['body'], 'x', game_state['board']['width'] - 1):
    is_move_safe["right"] = False
  elif my_head["y"] != game_state['board'][
      'height'] - mySnakeLength and my_head["x"] == game_state['board'][
        'width'] - 1 and checkIfBodyPartsInCornerDangerZone(
          game_state['you']['body'], 'y', game_state['board']['height'] - 1):
    is_move_safe["up"] = False

    # For bottom-left
  if my_head["x"] != mySnakeLength - 1 and my_head[
      "y"] == 0 and checkIfBodyPartsInCornerDangerZone(
        game_state['you']['body'], 'x', 0):
    is_move_safe["left"] = False
  elif my_head["y"] != mySnakeLength - 1 and my_head[
      "x"] == 0 and checkIfBodyPartsInCornerDangerZone(
        game_state['you']['body'], 'y', 0):
    is_move_safe["down"] = False

    # For bottom-right
  if my_head["x"] != game_state['board']['width'] - mySnakeLength and my_head[
      "y"] == 0 and checkIfBodyPartsInCornerDangerZone(
        game_state['you']['body'], 'x', game_state['board']['width'] - 1):
    is_move_safe["right"] = False
  elif my_head["y"] != mySnakeLength - 1 and my_head["x"] == game_state[
      'board']['width'] - 1 and checkIfBodyPartsInCornerDangerZone(
        game_state['you']['body'], 'y', 0):
    is_move_safe["down"] = False

  # if snake at the edge of the board: the top-bottom or left-right , prevent snake from colliding with each other due to lack of safe moves pre-emptively
  # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
  opponents = game_state['board']['snakes']
  # If we are bigger, and we are going to collide with enemy head, collide
  for opponentSnake in opponents:
    if opponentSnake['id'] != game_state['you']['id']:
      for opponentSnakeBody in opponentSnake['body']:

        if my_head["x"] - 1 == opponentSnakeBody["x"] and my_head[
            "y"] == opponentSnakeBody["y"]:
          is_move_safe["left"] = False
        elif my_head["x"] + 1 == opponentSnakeBody["x"] and my_head[
            "y"] == opponentSnakeBody["y"]:
          is_move_safe["right"] = False

        if my_head["y"] - 1 == opponentSnakeBody["y"] and my_head[
            "x"] == opponentSnakeBody["x"]:
          is_move_safe["down"] = False
        elif my_head["y"] + 1 == opponentSnakeBody["y"] and my_head[
            "x"] == opponentSnakeBody["x"]:
          is_move_safe["up"] = False

        xDirection = my_head["x"] - opponentSnake["head"]["x"]
        yDirection = my_head["y"] - opponentSnake["head"]["y"]

        if abs(xDirection) == 1 and abs(
            yDirection) == 1 and len(my_body) <= len(opponentSnake['body']):
          start()
          if xDirection == -1:
            is_move_safe["right"] = False
          elif xDirection == 1:
            is_move_safe["left"] = False
          if yDirection == 1:
            is_move_safe["down"] = False
          elif yDirection == -1:
            is_move_safe["up"] = False

        if (abs(xDirection) == 2 or abs(yDirection)
            == 2) and len(my_body) <= len(opponentSnake['body']):
          if xDirection == 2 and my_head["y"] == opponentSnake["head"]["y"]:
            is_move_safe["left"] = False
          elif xDirection == -2 and my_head["y"] == opponentSnake["head"]["y"]:
            is_move_safe["right"] = False
          if yDirection == 2 and my_head["x"] == opponentSnake["head"]["x"]:
            is_move_safe["down"] = False
          elif yDirection == -2 and my_head["x"] == opponentSnake["head"]["x"]:
            is_move_safe["up"] = False

  # Are there any safe moves left?
  safe_moves = []
  for move, isSafe in is_move_safe.items():
    if isSafe:
      safe_moves.append(move)

  if len(safe_moves) == 0:
    print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
    return {"move": "down"}

  # Choose a random move from the safe ones
  next_move = random.choice(safe_moves)

  # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
  # Try not to go into corner of board, calculate body position to determine safe corner
  food = game_state['board']['food']
  # FInd the closest one first
  # closest = {'totalDist': 0, 'x': 9999, 'y': 9999}
  # if {
  #     'x': closest['x'],
  #     'y': closest['y']
  # } not in food:
  #   closest['totalDist'] = 0
  # if closest['totalDist'] == 0:
  #   for dot in food:
  #       xDiff = abs(my_head["x"] - dot['x'])
  #       yDiff = abs(my_head["y"] - dot['y'])
  #       totalDist = xDiff + yDiff
  #       if totalDist > closest['totalDist']:
  #         closest['x'] = dot['x']
  #         closest['y'] = dot['y']
  #         closest['totalDist'] = totalDist

  if my_head['x'] > food[len(food) - 1]['x']:
    is_move_safe['right'] = False
  elif my_head['x'] < food[len(food) - 1]['x']:
    is_move_safe['left'] = False
  if my_head['y'] > food[len(food) - 1]['y']:
    is_move_safe['up'] = False
  elif my_head['y'] < food[len(food) - 1]['y']:
    is_move_safe['down'] = False

  next_move = random.choice(safe_moves)

  print(f"MOVE {game_state['turn']}: {next_move}")
  return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
  from server import run_server

  run_server({"info": info, "start": start, "move": move, "end": end})
