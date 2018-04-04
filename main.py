from standard_board import StandardBoard
import game
import curses


def render_board(x_off, y_off, board, stdscr, highlight=[]):
    for y in range(8):
        for x in range(8):
            # If square is light coloured (cyan)
            if((x+y) % 2 == 0):
                try:
                    if board.grid[y][x].team == "white":
                        c = curses.color_pair(1)
                    else:
                        c = curses.color_pair(3)
                except AttributeError:
                    c = curses.color_pair(1)
            # If square is dark coloured (blue)
            else:
                try:
                    if board.grid[y][x].team == "white":
                        c = curses.color_pair(2)
                    else:
                        c = curses.color_pair(4)
                except AttributeError:
                    c = curses.color_pair(2)

            try:
                highlight.index((x, y))
                if board.grid[y][x].team == "white":
                    c = curses.color_pair(5)
                else:
                    c = curses.color_pair(6)
            except ValueError:
                pass
            except AttributeError:
                c = curses.color_pair(5)
            # Check if square contains a piece and
            # set output char accordingly
            if isinstance(board.grid[y][x], game.Piece):
                i = board.grid[y][x].icon
            else:
                i = ' '

            # Print square to screen
            stdscr.addch(y+y_off, x+x_off, i, c)


def main(stdscr):
    # Enable Mouse
    curses.mousemask(True)
    # Disable Cursor
    curses.curs_set(0)

    # Initialize Color Pairs.
    # White piece
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    # Black piece
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
    # Board highlighting
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_GREEN)
    # Off-board
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Setup pieces
    board = StandardBoard()
    board_x = 2
    board_y = 2

    turn = "white"
    turn_count = 0
    stdscr.addstr(0, 1, "Turn:", curses.color_pair(7))

    # Main rendering loop
    while True:

        # Render board and pieces
        render_board(board_x, board_y, board, stdscr)
        stdscr.addstr(0, 6, str(turn), curses.color_pair(7))
        stdscr.refresh()

        piece_moved = False

        # Select a piece
        while True:
            event = stdscr.getch()
            if event == curses.KEY_MOUSE:
                try:
                    _, click_x, click_y, _, _ = curses.getmouse()
                except:
                    continue
            # If click was a valid piece
            if board.square_has_piece(click_x-board_x, click_y-board_y, turn):
                selected_piece = board.grid[click_y-board_y][click_x-board_x]
                avail_moves = selected_piece.valid_move_list(board)
                # Update render
                render_board(board_x, board_y, board, stdscr, avail_moves)
                stdscr.refresh()
                break

        # Select a target square
        while True:
            event = stdscr.getch()
            if event == curses.KEY_MOUSE:
                try:
                    _, click_x, click_y, _, _ = curses.getmouse()
                except:
                    continue
            try:
                avail_moves.index((click_x-board_x, click_y-board_y))
            except ValueError:
                break
            else:
                board.move_piece(selected_piece, click_x-board_x, click_y-board_y)
                piece_moved = True
                break

        if piece_moved:
            turn = game.opposite_team(turn)
            turn_count = turn_count + 1

        stdscr.refresh()
    # End main rendering loop


curses.wrapper(main)
