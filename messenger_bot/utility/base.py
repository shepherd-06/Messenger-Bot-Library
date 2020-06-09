from messenger_bot.utility.util import MessengerUtility
from messenger_bot.utility.tag import Tags
import logging


class BaseClass:
    """
    Base class is here to stop me from importing necessary stuff/classes/functions
    on every classes
    """

    def __init__(self):
        self.utility = MessengerUtility()
        self.tags = Tags
        self.logger = logging.getLogger('messenger_bot_library')
        __formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        __log_stream_handler = logging.StreamHandler()
        __log_stream_handler.setFormatter(__formatter)
        self.logger.setLevel(10)
        self.logger.addHandler(__log_stream_handler)
