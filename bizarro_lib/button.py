from bizarro_lib.tag import Tags
from bizarro_lib.mother import MotherClass
from bizarro_lib.button_validation import ButtonValidation


class Button(MotherClass):

    def __init__(self):
        super().__init__()
        self.btn_validation = ButtonValidation()
        

    def create_url_button(self, title: str, url: str, webview_height_ratio: str = "full", messenger_extensions: bool = False, fallback_url: str = '', webview_share_button: str = 'hide', is_default_action: bool = False):
        """
        Also applied as DEFAULT_ACTION in multiple other templates.
        Reference: https://developers.facebook.com/docs/messenger-platform/reference/buttons/url
        Supported usage:
            Persistent menu
            Generic template
            List template
            Button template
            Media template 
            Open graph template
        :title :str Button title. 20 character limit.
        :url :str This URL is opened in a mobile browser when the button is tapped. Must use HTTPS protocol if messenger_extensions is true.
        :webview_height_ratio :str Optional. Height of the Webview. Valid values: compact, tall, full. Defaults to full.
        :messenger_extensions :bool Optional. Must be true if using Messenger Extensions.
        :fallback_url :str The URL to use on clients that don't support Messenger Extensions. If this is not defined, the url will be used as the fallback. It may only be specified if messenger_extensions is true.
        :webview_share_button: str Optional. Set to hide to disable the share button in the Webview (for sensitive info). This does not affect any shares initiated by the developer using Extensions. 
        :returns a dictionary in the format for web_url button template
        """
        user = "create_url_button"
        if not is_default_action:
            if title is None or len(title) <= 0:
                self.zathura.insert_error_log(user, "title", "title is None or len is zero. Title: {}".format(
                    title), self.zathura_utility.Tag_Log_ERROR)
                return

            if len(title) > 20:
                # Error / Warning
                self.zathura.insert_error_log(user, "title", "title len is more than 20. Title: {}".format(
                    title), self.zathura_utility.Tag_Log_WARNING)
                pass

        if url is None or len(url) <= 0:
            # Error
            self.zathura.insert_error_log(
                user, "url", "url is None or len is zero. Url: {}".format(url), self.zathura_utility.Tag_Log_ERROR)
            return
        if not self.utility.url_validation(url):
            # Error
            self.zathura.insert_error_log(
                user, "url", "url did not validate itself as web_url. Url: {}".format(url), self.zathura_utility.Tag_Log_ERROR)
            return

        if webview_height_ratio not in (Tags.TAG_WEBVIEW_HEIGHT_RATIO_COMAPCT, Tags.TAG_WEBVIEW_HEIGHT_RATIO_FULL, Tags.TAG_WEBVIEW_HEIGHT_RATIO_TALL):
            # error
            self.zathura.insert_error_log(
                user, "webview_height_ratio", "webview_height_ratio did not match the 3 choices. webview_height_ratio: {}".format(webview_height_ratio), self.zathura_utility.Tag_Log_ERROR)
            return

        if messenger_extensions:
            if not self.utility.https_url_validation(url):
                # ERROR
                self.zathura.insert_error_log(
                    user, "url", "url has to be HTTPS if messenger_extensions is True. Url: {}".format(url), self.zathura_utility.Tag_Log_ERROR)

                return
            if fallback_url is None or len(fallback_url) == 0:
                # Error
                self.zathura.insert_error_log(
                    user, "fallback_url", "Fallback url has to be present if messenger_extension is True. fallback_url: {}".format(fallback_url), self.zathura_utility.Tag_Log_ERROR)

                return
            if not self.utility.https_url_validation(fallback_url):
                # Error
                self.zathura.insert_error_log(
                    user, "fallback_url", "Fallback url has to be HTTPS if messenger_extensions is True. fallback_url: {}".format(fallback_url), self.zathura_utility.Tag_Log_ERROR)

                return

        if not webview_share_button in (Tags.TAG_SHARE_HIDE, Tags.TAG_SHARE_SHOW):
            # Error
            self.zathura.insert_error_log(
                user, "webview_share_button", "webview_share_button value did not match the values required. Its either hide | show. webview_share_button: {}".format(webview_share_button), self.zathura_utility.Tag_Log_ERROR)
            return
        if is_default_action:
            if messenger_extensions:
                # These fields will only required if the messenger_extension is TRUE!
                self.logger.warning(
                    "Since messenger extension is True, fallback_url must be whitelisted on your page. Or else message won't be sent!")
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
                    "Since messenger extension is True, fallback_url must be whitelisted on your page. Or else message won't be sent!")
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
        Reference: https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback
        The postback button sends a messaging_postbacks event to your webhook with the string set in the payload property.
        This allows you to take an arbitrary actions when the button is tapped.
        For example, you might display a list of products,
        then send the product ID in the postback to your webhook,
        where it can be used to query your database and return the product details as a structured message.

        The postback button is supported for use with the following:
        - Persistent menu
        - Generic template
        - List template
        - Button template
        - Media template

        :title :str - Button title. 20 character limit.
        :payload :str - This data will be sent back to your webhook. 1000 character limit.
        """
        user = "create_postback_button"

        if title is None or title == '':
            # Error
            self.zathura.insert_error_log(
                user, "title", "title is None or empty string. Title: {}".format(title), warning=4)
            return

        if len(title) > 20:
            self.zathura.insert_error_log(user, "title", "title is more than 20 chars long. Title: {}".format(
                title), warning=self.zathura_utility.Tag_Log_WARNING)
            pass

        if payload is None or payload == '':
            # Error
            self.zathura.insert_error_log(
                user, "payload", "payload is None or empty string. Payload: {}".format(payload), warning=4)
            return

        if len(payload) > 1000:
            # Error
            self.zathura.insert_error_log(
                user, "payload", "payload is more than 1000 chars long. Payload: {}".format(payload), warning=4)
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_POSTBACK,
            Tags.TAG_TITLE: title,
            Tags.TAG_PAYLOAD: payload,
        }

    def create_call_button(self, title: str, phone_number: str):
        """
        Reference: https://developers.facebook.com/docs/messenger-platform/send-messages/buttons#call
        The call button dials a phone number when tapped. Phone number should be in the format +<COUNTRY_CODE><PHONE_NUMBER>, e.g. +15105559999.
        The call button is supported for use with the following:
        - Generic template
        - List template
        - Button template
        - Media template
        :title :str Button title, 20 character limit.
        :phone_number :str Format must have "+" prefix followed by the country code, area code and local number. For example, +16505551234.
        """
        import phonenumbers
        user = "create_log_in_button"

        if title is None or title == '':
            # Error
            self.zathura.insert_error_log(
                user, "title", "title is None or empty string. Title: {}".format(title), warning=4)
            return

        if len(title) > 20:
            self.zathura.insert_error_log(user, "title", "title is more than 20 chars long. Title: {}".format(
                title), warning=self.zathura_utility.Tag_Log_WARNING)
            pass

        if phone_number is None or phone_number == '':
            # Error
            self.zathura.insert_error_log(
                user, "phone_number", "phone_number is None or empty string. phone_number: {}".format(phone_number), warning=4)
            return
        try:
            _phone_number = phonenumbers.parse(phone_number, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            self.zathura.insert_error_log(
                user, "phone_number", "Missing or invalid default region. Phone number: {}".format(phone_number), warning=4)
            return

        if not phonenumbers.is_valid_number(_phone_number):
            # Error
            self.zathura.insert_error_log(
                user, "phone_number", "phone_number is not valid: {}".format(phone_number), warning=4)
            return

        return {
            Tags.TAG_TYPE: Tags.TAG_PHONE_NUMEBR,
            Tags.TAG_TITLE: title,
            Tags.TAG_PAYLOAD: phone_number,
        }

    def create_share_button(self, share_contents: dict = None):
        """
        Reference: https://developers.facebook.com/docs/messenger-platform/send-messages/buttons#share
        The share button allows the message recipient to share the content of a message you sent with others on Messenger. The name and icon of your Page appear as an attribution at the top of the shared content.
        The attribution opens a conversation with your bot when tapped.
        With the share button, you can share the exact message or specify a new generic template message in the share_contents property.
        If you specify a new generic template, the message recipient will be able to add a message to the share. This is useful if you want change the look or add content to the original message.

        The share button is supported for use with the following:
        - Generic template
        - List template
        - Media template
        :share_contents: dict For share buttons using the element_share feature,
            only the <generic template> with [[ one URL button ]] is supported.
            share_contents only supports the following:
                - Template used must be generic template.
                - Maximum of one URL button on the template. If no buttons are specified, 
                  the buttons property on the generic template must be set to an empty array.
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
