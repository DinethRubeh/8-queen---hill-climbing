import math
import random
 
def sim_anneal(board):
  temp = 3000
  anneal_rate = 0.98
  new_h = get_h(board)
   
  while new_h > 0:
    board = sim_anneal_move(board,new_h,temp)
    new_h = get_h(board)
    #to make sure that temp doesn't get too low
    new_temp = max(temp * anneal_rate,0.01)
    temp = new_temp
    if steps >= 60000:
      break
 
def sim_anneal_move(board,best_h,temp):
  board_1 = list(board)
  found_move = False
 
  while not found_move:
    board_1 = list(board)
    new_row = random.randint(0,len(board)-1)
    new_col = random.randint(0,len(board)-1)
    board_1[new_col] = new_row
    new_h = get_h(board_1)
    if new_h < best_h:
      found_move = True
    else:
      #check the badness of the move
      delta_e = best_h - new_h
      #probability accept level
      prob = min(1,math.exp(delta_e/temp))
      found_move = random.random() <= prob
   
  return board_1
