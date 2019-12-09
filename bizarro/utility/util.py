import re
from bizarro.utility.tag import Tags


class Utility:

    @staticmethod
    def url_validation(url: str):
        """
        url validation takes a str to be matched against regex.

        :type url: str
        :param url: "url" that needs to be validated!

        :returns: bool
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
        url validation takes a str to be matched against regex. This is if the url has to be https.

        :type url: str
        :param url: "url" that needs to be validated in https or ftps (secure) format.

        :returns: bool
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
        Creates the template for recipient. I use it to generate the recipients in every cases.

        :type user_id: str
        :param user_id: facebook users user_id.

        :return: :dict
        """
        return {
            Tags.TAG_RECIPIENT: {
                Tags.TAG_ID: user_id
            }
        }

    def typing_on(self, user_id: str, waiting_period: float = 1.5):
        """
        Creates a payload for typing_on function. However, if your code sends any message before the waiting period, the typing_on function will disappear. You have to wait before sending the message.

        :type waiting_period: float
        :param waiting_period: Amount of seconds to wait aka show typing_on icon on messenger platform
        :type user_id: str
        :param user_id: facebook user_id

        :return: :dict
        """
        payload = self.create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_TYPING_ON
        return payload

    def marked_seen(self, user_id):
        """
        Creates a payload so you can mark the last message as seen.

        :type user_id: str
        :param user_id: facebook user id

        :return: :dict
        """
        payload = self.create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_MARK_SEEN
        return payload

    def basic_text_reply_payload(self, user_id: str, message: str):
        """
        this functions generates the payload for basic text reply. sends the string for *message* as a normal message.

        :type user_id: str
        :param user_id: user_id of a particular user_id
        :type message: str
        :param message: message user is going to see. *Message text cannot be None and must be less than **2000 characters**.*

        :returns: :dict
        """
        if message is None or len(message) > 2000:
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
    def whitelist_domain(url: str):
        """
        Creates a payload for domain whitelist. You should not use it. It's experimental.

        :type url: str
        :param url: url that has to be whitelisted

        :returns: :dict
        """
        return {
            Tags.TAG_WHITELISTED_DOMAINS: url,
        }
