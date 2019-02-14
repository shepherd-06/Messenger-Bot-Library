from ZathuraProject.zathura import Zathura
from ZathuraProject.utility import Utility as zathura_utility
from BotLib.utility.util import Utility
from BotLib.utility.tag import Tags


class MotherClass:
    """
    Mother classs is here to stop me from importing necessary stuff/classes/functions on every classes
    """

    def __init__(self):
        self.zathura = Zathura()
        self.zathura_utility = zathura_utility()
        self.utility = Utility()
        self.tags = Tags
