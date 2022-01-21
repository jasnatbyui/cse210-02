from game.die import Die

class director:


    def __init__(self):

        self.hilo = Die()
        self.is_playing = True
        self.score = 300
        self.total_score = 0

    def start_game(self):

        while self.is_playing:

            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        ask_player = input("")
            