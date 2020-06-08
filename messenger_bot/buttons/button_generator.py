from messenger_bot.utility.tag import Tags
from messenger_bot.utility.base import BaseClass
from messenger_bot.buttons.button_validator import ButtonValidation


class Button(BaseClass):
    """
    Button class Generates multiple types of button to use in different templates and replies for Messenger Bot Platform. Currently supported button types are:

        * Url Button
        * Postback Button
        * Call Button
        * *Share Button* (This might be little buggy! I have not been able to run a full test on it yet)

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
           * List template
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
        user = "create_url_button"
        if not is_default_action:
            if title is None or len(title) <= 0:
                return

            if len(title) > 20:
                # Error / Warning
                pass

        if url is None or len(url) <= 0:
            # Error
            return
        if not self.utility.url_validation(url):
            # Error
            return

        if webview_height_ratio not in (
                Tags.TAG_WEBVIEW_HEIGHT_RATIO_COMAPCT, Tags.TAG_WEBVIEW_HEIGHT_RATIO_FULL,
                Tags.TAG_WEBVIEW_HEIGHT_RATIO_TALL):
            # error
            return

        if messenger_extensions:
            if not self.utility.https_url_validation(url):
                # ERROR
                return
            if fallback_url is None or len(fallback_url) == 0:
                # Error
                return
            if not self.utility.https_url_validation(fallback_url):
                # Error
                return

        if not webview_share_button in (Tags.TAG_SHARE_HIDE, Tags.TAG_SHARE_SHOW):
            # Error
            return
        if is_default_action:
            if messenger_extensions:
                # These fields will only required if the messenger_extension is TRUE!
                self.logger.warning(
                    "Since messenger extension is True, fallback_url must be whitelisted on your page. Or else "
                    "message won't be sent!")
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
                # These fields will only required if the messenger_extension is TRUE!
                self.logger.warning(
                    "Since messenger extension is True, fallback_url must be whitelisted on your page. Or else "
                    "message won't be sent!")
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
        user = "create_postback_button"

        if title is None or title == '':
            # Error
            return

        if len(title) > 20:
            pass

        if payload is None or payload == '':
            # Error
            return

        if len(payload) > 1000:
            # Error
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
        user = "create_log_in_button"

        if title is None or title == '':
            # Error
            return

        if len(title) > 20:
            pass

        if phone_number is None or phone_number == '':
            # Error
            return
        try:
            _phone_number = phonenumbers.parse(phone_number, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            return

        if not phonenumbers.is_valid_number(_phone_number):
            # Error
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_PHONE_NUMEBR,
            Tags.TAG_TITLE: title,
            Tags.TAG_PAYLOAD: phone_number,
        }

    def create_share_button(self, share_contents: dict = None):
        """
        **Reference:** https://developers.facebook.com/docs/messenger-platform/send-messages/buttons#share

        The share button allows the message recipient to share the content of a message you sent with others on Messenger. The name and icon of your Page appear as an attribution at the top of the shared content.
        The attribution opens a conversation with your bot when tapped.
        With the share button, you can share the exact message or specify a new generic template message in the share_contents property.
        If you specify a new generic template, the message recipient will be able to add a message to the share. This is useful if you want change the look or add content to the original message.

        The share button is supported for use with the following:
            * Generic template
            * List template
            * Media template

        :type share_contents: dict
        :param share_contents: For share buttons using the element_share feature, only the **Generic Template** with *one URL button* is supported.

        *share_contents* only supports the following:
                * Template used must be generic template.
                * Maximum of one URL button on the template.
                * If no buttons are specified, the buttons property on the generic template must be set to an empty array.

        :return: creates a payload which enable user to share the content of a message.
        """
        if share_contents is None:
            return {
                "type": "element_share"
            }
        else:
            """
            To create a share element, I will send a request to generic_element to 
            create_single_generic_elements function. This will run an initial validation
            against the parameters given, however, this won't pass for share element
            so I will send the share_element to btn_validation class to validate again.
            User will:
            1) create a default_action btn from btn class
            2) create a btn array 
            3) call create_single_generic_elements function
            4) send the package to generate_generic_payload
            5) that would be share_elements which comes here
            This shit is little confusing at this moment. I think i need to trim it down a little bit later
            """
            if not self.btn_validation.validate_generic_share_elements(share_contents):
                return {
                    self.tags.TAG_TYPE: self.tags.TAG_ELEMENT_SHARE,
                    self.tags.TAG_SHARE_CONTENTS: share_contents
                }
            else:
                return None
