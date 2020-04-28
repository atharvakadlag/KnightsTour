import pprint
pp = pprint.PrettyPrinter()

def isSafe(new_x, new_y, board):
    if (0 <= new_x < 8 and 0 <= new_y < 8 and board[new_x][new_y]==-1):
    	return True
    return False

def print_board(board):
	pp.pprint(board)

def tour(curr_x,curr_y,move_x,move_y,board,pos):
	if pos == 64:
		return True

	for i in range(8):
		new_x = curr_x+move_x[i]
		new_y = curr_y+move_y[i]
		if isSafe(new_x,new_y,board):
			board[new_x][new_y] = pos
			if tour(new_x, new_y, move_x,move_y, board, pos+1):
				return True

			board[new_x][new_y]=-1

	return False

if __name__ == '__main__':

	move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
	move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
	board = [[-1 for i in range(8)]for i in range(8)]

	board[0][0]=0

	if tour(0,0,move_x,move_y,board,1):
		print_board(board)
	else:
		print("error")
