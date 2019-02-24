from bizarro_lib.utility.mother import MotherClass
from bizarro_lib.utility.button_validation import ButtonValidation


class ListTemplate(MotherClass):

    def __init__(self, fb_user_id):
        super().__init__()
        self.user_id = fb_user_id
        self.btn_validation = ButtonValidation()

    def validate_list_element(self, title: str, subtitle: str = None, image_url: str = None, default_action: dict = None, buttons: list = None):
        """
        :title :str String to display as the title of the list item. 80 character limit. May be truncated if the title spans too many lines.
        :subtitle :str Optional. String to display as the subtitle of the list item. 80 character limit. May be truncated if the subtitle spans too many lines. 
                       Element must have one or both of image_url or subtitle set.
        :image_url :str Optional. URL of the image to display in the list item.
        :default_action :dict Optional. URL button that specifies the default action to execute when the list item is tapped.
                            Only allowed when messenger_extensions property is set to true
        :buttons :list Optional. Button to display on the list item. Maximum of 1 button is supported.
        """
        if title is None or len(title) == 0:
            # Error
            return False

        if subtitle is None and image_url is None:
            # Error
            return False

        if len(subtitle) == 0 and len(image_url) == 0:
            # Error
            return False

        if image_url is not None and len(image_url) != 0:
            if not self.utility.url_validation(image_url):
                # Error
                return False

        if default_action is not None:
            # check validation
            _type = default_action[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in default_action else None
            _url = default_action[self.tags.TAG_URL] if self.tags.TAG_URL in default_action else None
            _messenger_extension = default_action[self.tags.TAG_MESSENGER_EXTENSION] if self.tags.TAG_MESSENGER_EXTENSION in default_action else None
            _fallback_url = default_action[self.tags.TAG_FALLBACK_URL] if self.tags.TAG_FALLBACK_URL in default_action else None

            if _type != self.tags.TAG_WEB_URL:
                # Error
                return False

            if type(_messenger_extension) != bool:
                # Error
                return False

            if not _messenger_extension:
                # Error
                return False

            if _url is None or len(_url) == 0:
                # Error
                return False

            if not self.utility.url_validation(_url):
                # Error
                return False

            if _fallback_url is None or len(_fallback_url) == 0:
                # Error
                return False

            if not self.utility.https_url_validation(_fallback_url):
                # Error
                return False

        if buttons is not None:
            # check validation
            if type(buttons) != list:
                # error
                return False

            if len(buttons) > 1:
                # Error
                return False

            # button validation
            if type(buttons[0]) != dict:
                # Error
                return False

            if not self.btn_validation.button_validation(buttons[0]):
                # Error
                return False

        if default_action is None and buttons is None:
            # Error - both cannot None (may be)
            pass

    def create_list_element(self, title: str, subtitle: str = None, image_url: str = None, default_action: dict = None, buttons: list = None):
        """
        :title :str String to display as the title of the list item. 80 character limit. May be truncated if the title spans too many lines.
        :subtitle :str Optional. String to display as the subtitle of the list item. 80 character limit. May be truncated if the subtitle spans too many lines. 
                       Element must have one or both of image_url or subtitle set.
        :image_url :str Optional. URL of the image to display in the list item.
        :default_action :dict Optional. URL button that specifies the default action to execute when the list item is tapped.
                            Only allowed when messenger_extensions property is set to true
        :buttons :list Optional. Button to display on the list item. Maximum of 1 button is supported.
        """
        if not self.validate_list_element(title, subtitle, image_url, default_action, buttons):
            return
        else:
            # validation passed
            return {
                self.tags.TAG_TITLE: title,
                self.tags.TAG_SUBTITLE: subtitle,
                self.tags.TAG_IMAGE_URL: image_url,
                self.tags.TAG_DEFAULT_ACTION: default_action,
                self.tags.TAG_BUTTONS: buttons
            }

    def list_element(self, elements: list, top_element_style: str = "compact", buttons: list = None, sharable: bool = False):
        """
        :elements :list Array of objects that describe items in the list. 
                        Minimum of 2 elements required. Maximum of 4 elements is supported.
        :top_element_style :str Optional. Sets the format of the first list items. Messenger web client currently only renders compact.
                                compact: Renders a plain list item.
                                large: Renders the first list item as a cover item.
        :buttons :list Optional. Button to display at the bottom of the list. 
                        Maximum of 1 button is supported
        :sharable :bool Optional. Set to true to enable the native share button in Messenger for the template message. 
                        Defaults to false.
        """
        if elements is None:
            return

        if type(elements) != list:
            return

        if len(elements) < 2 or len(elements) > 4:
            return

        for element in elements:
            # validate every element piece by piece
            _title = element[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in element else None
            _subtitle = element[self.tags.TAG_SUBTITLE] if self.tags.TAG_SUBTITLE in element else None
            _image_url = element[self.tags.TAG_IMAGE_URL] if self.tags.TAG_IMAGE_URL in element else None
            _default_action = element[self.tags.TAG_DEFAULT_ACTION] if self.tags.TAG_DEFAULT_ACTION in element else None
            _buttons = element[self.tags.TAG_BUTTONS] if self.tags.TAG_BUTTONS in element else None

            if not self.validate_list_element(_title, _subtitle, _image_url, _default_action, _buttons):
                return

        if buttons is not None:
            if type(buttons) != list:
                return

            if len(buttons) > 1:
                return

            if len(buttons) != 0:
                if type(buttons[0]) != dict:
                    return

                if not self.btn_validation.button_validation(buttons[0]):
                    return

        if top_element_style not in (self.tags.TAG_ELEMENT_LARGE, self.tags.TAG_ELEMENT_COMPACT):
            return

        if type(sharable) != bool:
            return

        payload = {
            self.tags.TAG_TEMPLATE_TYPE: self.tags.TAG_LIST,
            self.tags.TAG_TOP_ELEMENT_STYLE: top_element_style,
            self.tags.TAG_BUTTONS: buttons,
            self.tags.TAG_ELEMENTS: elements,
            self.tags.TAG_SHAREABLE: sharable,
        }
        message = {
            self.tags.TAG_ATTACHMENT: {
                self.tags.TAG_TYPE: self.tags.TAG_TEMPLATE,
                self.tags.TAG_PAYLOAD: payload,
            }
        }

        list_element_payload = self.utility.create_basic_recipient(
            self.user_id)
        list_element_payload[self.tags.TAG_MESSAGE] = message
        return list_element_payload
