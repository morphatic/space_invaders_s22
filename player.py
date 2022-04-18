"""
Player
"""
import curses
from laser import Laser


class Player:
    def __init__(self, stdscr, window):
        self.stdscr = stdscr
        self.width = 6
        self.window = window
        self.range = (
            0,
            self.window[1] - self.width,
        )  # range of valid x values for the player
        self.speed = 1
        self.color = 3
        self.x = (
            self.window[1] // 2
        )  # puts the player in the middle of the screen (horizontally)
        self.y = self.window[0] - 5  # bottom of the screen (vertically)
        self.lasers = []

    def draw(self):
        self.stdscr.erase()  # why is this here and not in the Game class?
        self.stdscr.addstr(
            self.y, self.x, " " * self.width, curses.color_pair(self.color)
        )

    def tick(self, tick_number):
        [laser.tick(tick_number) for laser in self.lasers]
        self._handle_user_input()
        self.draw()

    def _handle_user_input(self):
        instruction = self.stdscr.getch()

        if instruction == curses.KEY_LEFT:
            x = self.x - 1
        elif instruction == curses.KEY_RIGHT:
            x = self.x + 1
        else:
            x = self.x

        if instruction == ord(" "):
            self.lasers.append(Laser(self.stdscr, self.x, self.y))

        # Ensure we don't drive off the board
        x = min(x, max(self.range))
        x = max(x, min(self.range))
        x = x - self.x

        self.x += x
