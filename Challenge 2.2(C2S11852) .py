class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        """
        Simulates a batsman playing.
        """
        print(f"{self.name} is batting.")

class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        """
        Simulates a bowler bowling.
        """
        print(f"{self.name} is bowling.")
batsman = Batsman("Sachin Tendulkar")
bowler = Bowler("Wasim Akram")
batsman.play()
bowler.play()