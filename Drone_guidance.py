# JHUB Coding scheme pyhton drone guidance

import os
import sys

# Import file name and error if wrong name, add stop feature

while True:
  filename = input("Enter file name: ")
  if filename == 'stop':
    sys.exit()
  elif not os.path.exists(filename):
    print("File does not exist")
    continue
# Split file into lists  
  with open(filename, "r") as readfile:
    track = readfile.read()
    moves = track.split('\n')
# x and y into coordinate (running upside down now for some reason, swapped x and y over to change from 90 degrees out)    
  x_pos = int(moves[0])
  y_pos = int(moves[1])
# It's plotting upside down because of the way the grid is printed so reverse the y axis and prints correctly
  y_pos = 13 - y_pos
  start_pos = [y_pos, x_pos]
  co_ord_x = y_pos
  co_ord_y = x_pos
# Add start position to blank list of coords
  coordinates = []
  coordinates.append(start_pos)
# Remove starting position so moves can be iterated through  
  del moves[0:2]
# Take directions off list and chance them into plotted points from start
  def grid_moves(co_ord_x, co_ord_y):
    for i in moves:
      if co_ord_x < 1 or co_ord_x > 12:
          print("Error: x-axis invalid.")
          break
      elif co_ord_y < 1 or co_ord_y > 12:
          print("Error: y-axis invalid.")
          break
      else:
          if i == "S":
              co_ord_y += 1
          elif i == "N":
              co_ord_y -= 1
          elif i == "E":
              co_ord_x += 1
          elif i == "W":
              co_ord_x -= 1
          coordinates.append([co_ord_y, co_ord_x])
    return coordinates 
# Create blank grid 12 x 12
  def create_blank_grid():
    grid_size = 12
    return [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
# Place the X's on the grid
  def place_x(grid, coordinates):
    for x, y in coordinates:
        grid[x - 1][y - 1] = 'X'

  def print_grid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 1))

  if __name__ == "__main__":
    blank_grid = create_blank_grid()

    place_x(blank_grid, grid_moves(x_pos, y_pos))
    print_grid(blank_grid)
    print(coordinates)
