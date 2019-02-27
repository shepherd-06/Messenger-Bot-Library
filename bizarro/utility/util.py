import re
from bizarro.utility.tag import Tags
from ZathuraProject.zathura import Zathura
from ZathuraProject.utility import Utility as zathura_utility


class Utility:

    def __init__(self):
        self.zathura = Zathura()
        self.z_utility = zathura_utility()

    @staticmethod
    def url_validation(url: str):
        """
        url validation takes a str to be matched against regex.
        :url the url in str
        :returns bool
        """
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url)

    @staticmethod
    def https_url_validation(url: str):
        """
        url validation takes a str to be matched against regex.
        :url the url in str
        :returns bool
        """
        regex = re.compile(
            r'^(?:https|ftps)?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url)

    @staticmethod
    def create_basic_recipient(user_id: str):
        """
        :param user_id: facebook users user id.
        :return: creates the receipients payload
        """
        return {
            Tags.TAG_RECIPIENT: {
                Tags.TAG_ID: user_id
            }
        }

    def typing_on(self, user_id: str, waiting_period: float = 1.5):
        """
        private function, turns on typing function, sleep 3s before doing anything else.
        :param user_id:
        :return: returns the payload for typing_on function
        """
        payload = self.create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_TYPING_ON
        return payload

    def marked_seen(self, user_id):
        """
        marked last message as seen in case there is no definitive action to be taken!
        :param user_id: facebook user id
        :return: payload to create a mark_seen on facebook messenger platform
        """
        payload = self.create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_MARK_SEEN
        return payload

    def basic_text_reply_payload(self, user_id: str, message: str):
        """
        this functions generates the payload for basic text reply
        :param user_id: user_id of a particular user_id
        :param message: message user going to see
        :return: payload
        """
        if message is None or len(message) > 2000:
            self.zathura.insert_error_log(user=user_id, error_name="message length exceeds limit or None",
                                          error_description="Either message length exceeds 2000 characters limit or None. Message: {}".format(message), warning=self.z_utility.Tag_Log_ERROR)
            return None

        payload = {
            Tags.TAG_RECIPIENT: {
                Tags.TAG_ID: user_id
            },
            Tags.TAG_MESSAGE: {
                Tags.TAG_TEXT: message
            }
        }
        return payload

    @staticmethod
    def whitelist_domain(url):
        return {
            Tags.TAG_WHITELISTED_DOMAINS: url,
        }
