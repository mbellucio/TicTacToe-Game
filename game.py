import time
from random import shuffle


class TicTacToe:
    
    def __init__(self):
        self.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.board_coord = {'1': 0, '2': 1, '3': 2, 'a': 0, 'b': 1,'c': 2}
        self.played_coords = []
        self.player_plays = []
        self.ai_plays = []
        self.all_coords = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        self.winning_sequences = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        self.play_counter = 0


    def print_board(self):
        print(
            f"\n      1     2     3\n"
            f"\nA     {self.game_board[0][0]}  |  {self.game_board[0][1]}  |  {self.game_board[0][2]}  \n"
            f"    -----------------\n"
            f"B     {self.game_board[1][0]}  |  {self.game_board[1][1]}  |  {self.game_board[1][2]}  \n"
            f"    -----------------\n"
            f"C     {self.game_board[2][0]}  |  {self.game_board[2][1]}  |  {self.game_board[2][2]}  \n"
        )


    def get_play(self, coord:str, player:str):
        turn_play = []
        for ch in coord:
            xy = self.board_coord[ch]
            turn_play.append(xy)
        if player == 'player':
            p = 'X'
        else: 
            p = 'O'
        self.game_board[turn_play[0]][turn_play[1]] = p
        self.play_counter += 1
        return self.print_board()


    def player_turn(self):
        p_entry = input("Type coordinates(ex: A1) :> ").lower()
        if p_entry in self.played_coords:
            print(" This place already been played, choose another one!")
            return self.player_turn()
        else:
            self.played_coords.append(p_entry)
            self.player_plays.append(p_entry)
            self.all_coords.remove(p_entry)
        self.get_play(p_entry, 'player')


    def end_game(self):
        for item in self.winning_sequences:
            result = all(elem in self.ai_plays for elem in item)
            if result:
                print('AI Wins!')
                return True

        for item in self.winning_sequences:
            result = all(elem in self.player_plays for elem in item)
            if result:
                print('Player Wins!')
                return True

        if self.play_counter == 9:
            print('It is a Tie!')
            return True


    def ai_turn(self):
            time.sleep(0.7)
            play = None

            # everytime AI plays it ramdomizes the winning sequence list, to not make ai previsible and exploitable
            shuffle(self.winning_sequences)

            #AI will defend if player near winning sequence(2/3)
            for item in self.winning_sequences:
                played_coords = []
                non_played_coords = []
                for coord in item:
                    if coord in self.player_plays:
                        played_coords.append(coord)
                    else:
                        if coord not in self.ai_plays:
                            non_played_coords.append(coord)
                        else: 
                            continue
                if len(played_coords) == 2 and len(non_played_coords) == 1:
                    play = non_played_coords[0]
                continue
                
            # when not defending AI will search for a possible sequence to win
            if play == None:
                for item in self.winning_sequences:
                    result = any(elem in self.player_plays for elem in item)
                    if not result:
                        for coord in item:
                            if coord not in self.ai_plays:
                                play = coord
            
            self.get_play(play, 'ai')
            self.played_coords.append(play)
            self.ai_plays.append(play)
            self.all_coords.remove(play)


    def play_game(self):
        self.print_board()
        while not self.end_game():
            self.player_turn()
            if self.end_game():
                break
            self.ai_turn()



