from bizarro.utility.util import Utility
from bizarro.utility.tag import Tags
import logging


class MotherClass:
    """
    Mother class is here to stop me from importing necessary stuff/classes/functions
    on every classes
    """

    def __init__(self):
        self.utility = Utility()
        self.tags = Tags
        self.logger = logging.getLogger('bizarro')
        __formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        __log_stream_handler = logging.StreamHandler()
        __log_stream_handler.setFormatter(__formatter)
        self.logger.setLevel(10)
        self.logger.addHandler(__log_stream_handler)
