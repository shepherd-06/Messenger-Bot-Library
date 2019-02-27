from ZathuraProject.zathura import Zathura
from ZathuraProject.utility import Utility as zathura_utility
from bizarro_lib.util import Utility
from bizarro_lib.tag import Tags
import logging


class MotherClass:
    """
    Mother classs is here to stop me from importing necessary stuff/classes/functions on every classes
    """

    def __init__(self):
        self.zathura = Zathura()
        self.zathura_utility = zathura_utility()
        self.utility = Utility()
        self.tags = Tags
        self.logger = logging.getLogger('bizarro')
        __formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        __log_stream_handler = logging.StreamHandler()
        __log_stream_handler.setFormatter(__formatter)
        self.logger.setLevel(10)
        self.logger.addHandler(__log_stream_handler)
