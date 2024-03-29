from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from players import ConsolePlayer
from renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
