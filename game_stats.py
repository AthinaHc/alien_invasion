class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start the game in an inactive state.
        self.game_active = False

        #High score should never be reset
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def write_high_score(self):
        with open("HighScore.txt", "w") as file_w:
            file_w.write(str(self.high_score))
        

    def read_high_score(self):
        try:
            with open("HighScore.txt", "r") as file_r:
                high_score = int(file_r.read())
                return high_score
        except FileNotFoundError:
            return 0
