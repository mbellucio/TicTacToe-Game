from game import TicTacToe


def start_game():
    game = TicTacToe()
    response = input("\nWould you like to play TicTacToe? Y/N :> ").lower()
    if response == 'y':
        game.play_game()
        start_game()


start_game()

