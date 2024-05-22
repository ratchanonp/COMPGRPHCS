class Overview:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def render(self, delta_time):
        self.display.fill('blue')

    def update(self, delta_time):
        pass