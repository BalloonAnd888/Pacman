class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        # self.screen_width = 1200
        # self.screen_height = 800
        # self.bg_color = (0, 0, 0)
        # self.bg_color = (150, 150, 150)
        self.tilewidth = 32
        self.tileheight = 32
        self.nrows = 20
        self.ncols = 28
        self.screen_width = self.ncols*self.tilewidth
        self.screen_height = self.nrows*self.tileheight
        # self.screensize = (self.screen_width, self.screen_height)
        self.black = (0, 0, 0)
        self.yellow = (255, 255, 0)
        self.initialize_speed_settings()
        self.posn = 0

    def initialize_speed_settings(self):
        self.pacman_speed_factor = 0.15
        self.ghost_speed_factor = 1



