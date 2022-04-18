"""
The main program file that runs everything
"""
import curses

from curses import wrapper
from game import Game


def main(stdscr):
    curses.curs_set(False)  # makes the cursor invisible (sets visibility to False)

    stdscr.nodelay(
        True
    )  # immediately handle user input (don't wait for "return" to be pressed)
    stdscr.clear()

    Game(stdscr).run()


if __name__ == "__main__":
    wrapper(main)
