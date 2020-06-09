import logging

from messenger_bot.buttons.button_validator import ButtonValidation
from messenger_bot.utility.base import BaseClass
from messenger_bot.utility.tag import Tags


class Button(BaseClass):
    """
    Button class Generates multiple types of button to use in different templates and replies for Messenger Bot Platform. Currently supported button types are:

        * Url Button
        * Postback Button
        * Call Button

    Please check Facebook's documentation for more information. See the **Reference** url on top of every buttons.
    """

    def __init__(self):
        super().__init__()
        self.btn_validation = ButtonValidation()

    def create_url_button(self, title: str, url: str,
                          webview_height_ratio: str = "full",
                          messenger_extensions: bool = False,
                          fallback_url: str = '',
                          webview_share_button: str = 'hide',
                          is_default_action: bool = False):
        """
        Also applied as DEFAULT_ACTION in multiple other templates.
        **Reference**: https://developers.facebook.com/docs/messenger-platform/reference/buttons/url

        Supported usage:
           * Persistent menu
           * Generic template
           * Button template
           * Media template
           * Open graph template

        :type title: string
        :param title: Button title. 20 character limit.
        :type url: string
        :param url: This URL is opened in a mobile browser when the button is tapped. Must use HTTPS protocol if messenger_extensions is true.
        :type webview_height_ratio: string
        :param webview_height_ratio: *Optional*. Height of the Webview. Valid values: compact, tall, full. Defaults to full.
        :type messenger_extensions: string
        :param messenger_extensions: *Optional*. Must be true if using Messenger Extensions.
        :type fallback_url: string
        :param fallback_url: The URL to use on clients that don't support Messenger Extensions. If this is not defined, the url will be used as the fallback. It may only be specified if messenger_extensions is true.
        :type webview_share_button: string
        :param webview_share_button: *Optional*. Set to hide to disable the share button in the Webview (for sensitive info). This does not affect any shares initiated by the developer using Extensions.

        :returns: a dictionary in the format for web_url button template
        """
        if not is_default_action:
            if title is None or len(title) <= 0:
                logging.error(
                    "create_url_button - title is None or title is empty string")
                return

            if len(title) > 20:
                # Error / Warning
                logging.warn(
                    "create_url_button - title has more than 20 characters")
        else:
            title = ""

        if url is None or len(url) <= 0:
            # Error
            logging.error(
                "create_url_button - url is None or url is an empty string")
            return
        if not self.utility.url_validation(url):
            # Error
            logging.error("create_url_button - URL validation failed")
            return

        if webview_height_ratio not in (
                Tags.TAG_WEBVIEW_HEIGHT_RATIO_COMAPCT, Tags.TAG_WEBVIEW_HEIGHT_RATIO_FULL,
                Tags.TAG_WEBVIEW_HEIGHT_RATIO_TALL):
            # error
            logging.error(
                "create_url_button - webview height ratio option error")
            return

        if messenger_extensions:
            logging.info(
                "create_url_button - fallback URL has to be added on whitelist domain list.")
            if not self.utility.https_url_validation(url):
                # ERROR
                logging.error(
                    "create_url_button - HTTPS URL validation failed for messenger extension")
                return
            if fallback_url is None or len(fallback_url) == 0:
                # Error
                logging.error(
                    "create_url_button - Fallback URL is required in messenger extension")
                return
            if not self.utility.https_url_validation(fallback_url):
                # Error
                logging.error(
                    "create_url_button - Fallback URL has to be HTTPS for messenger extension")
                return

        if not webview_share_button in (Tags.TAG_SHARE_HIDE, Tags.TAG_SHARE_SHOW):
            # Error
            logging.error(
                "create_url_button - webview share button option is invalid")
            return
        if is_default_action:
            if messenger_extensions:
                # These fields will only required if the messenger_extension is TRUE!
                return {
                    Tags.TAG_TYPE: Tags.TAG_WEB_URL,
                    Tags.TAG_URL: url,
                    Tags.TAG_WEBVIEW_HEIGHT_RATIO: webview_height_ratio,
                    Tags.TAG_MESSENGER_EXTENSION: messenger_extensions,
                    Tags.TAG_FALLBACK_URL: fallback_url,
                }
            else:
                return {
                    Tags.TAG_TYPE: Tags.TAG_WEB_URL,
                    Tags.TAG_URL: url,
                    Tags.TAG_WEBVIEW_HEIGHT_RATIO: webview_height_ratio,
                }
        else:
            if messenger_extensions:
                return {
                    Tags.TAG_TYPE: Tags.TAG_WEB_URL,
                    Tags.TAG_URL: url,
                    Tags.TAG_TITLE: title,
                    Tags.TAG_WEBVIEW_HEIGHT_RATIO: webview_height_ratio,
                    Tags.TAG_MESSENGER_EXTENSION: messenger_extensions,
                    Tags.TAG_FALLBACK_URL: fallback_url,
                }
            else:
                return {
                    Tags.TAG_TYPE: Tags.TAG_WEB_URL,
                    Tags.TAG_URL: url,
                    Tags.TAG_TITLE: title,
                    Tags.TAG_WEBVIEW_HEIGHT_RATIO: webview_height_ratio,
                }

    def create_postback_button(self, title: str, payload: str):
        """
        **Reference:** https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback

        The postback button sends a messaging_postbacks event to your webhook with the string set in the payload property.
        This allows you to take an arbitrary actions when the button is tapped.
        For example, you might display a list of products,
        then send the product ID in the postback to your webhook,
        where it can be used to query your database and return the product details as a structured message.

        The postback button is supported for use with the following:
        * Persistent menu
        * Generic template
        * List template
        * Button template
        * Media template

        :type title: string
        :param title: Button title. 20 character limit.
        :type payload: string
        :param payload: This data will be sent back to your webhook. 1000 character limit.

        :return: A postback type button payload
        """
        if title is None or title == '':
            # Error
            logging.error(
                "create_postback_button - title is None or title is empty string")
            return

        if len(title) > 20:
            logging.warn(
                "create_postback_button - title has more than 20 characters")
            pass

        if payload is None or payload == '':
            # Error
            logging.error(
                "create_postback_button - payload is None or empty string")
            return

        if len(payload) > 1000:
            # Error
            logging.error(
                "create_postback_button - payload has more than 1000 characters")
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_POSTBACK,
            Tags.TAG_TITLE: title,
            Tags.TAG_PAYLOAD: payload,
        }

    def create_call_button(self, title: str, phone_number: str):
        """
        **Reference:** https://developers.facebook.com/docs/messenger-platform/send-messages/buttons#call

        The call button dials a phone number when tapped. Phone number should be in the format +<COUNTRY_CODE><PHONE_NUMBER>, e.g. +15105559999.

        The call button is supported for use with the following:
            * Generic template
            * List template
            * Button template
            * Media template

        :type title: string
        :param title: Button title, 20 character limit.
        :type phone_number: string
        :param phone_number: Format must have "+" prefix followed by the country code, area code and local number. For example, +16505551234.

        :return: Returns a button payload which enables the user to dial a certain number. Number might appear on their dial-pad. User have to manually press the dial button
        """
        import phonenumbers
        
        if title is None or title == '':
            # Error
            logging.error("create_call_button - title is None or empty string")
            return

        if len(title) > 20:
            logging.warn("create_call_button - title has more than 20 characters")
            pass

        if phone_number is None or phone_number == '':
            # Error
            logging.error("create_call_button - phone_number is None or empty string.")
            return
        try:
            _phone_number = phonenumbers.parse(phone_number, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            logging.error("create_call_button - phone_number parse exception")
            return

        if not phonenumbers.is_valid_number(_phone_number):
            # Error
            logging.error("create_call_button - phone_number is invalid")
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_PHONE_NUMEBR,
            Tags.TAG_TITLE: title,
            Tags.TAG_PAYLOAD: phone_number,
        }
