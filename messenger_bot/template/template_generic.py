import logging

from messenger_bot.buttons.button_validator import ButtonValidation
from messenger_bot.utility.base import BaseClass


class GenericTemplate(BaseClass):

    def __init__(self, facebook_user_id):
        super().__init__()
        self.user_id = facebook_user_id
        self.btn_validation = ButtonValidation()

    def generic_template(self, elements: list, shareable: bool = False, image_aspect_ratio: str = "horizontal"):
        """
        The generic template allows you to send a structured message that includes an image, text and buttons.
        A generic template with multiple templates described in the elements array will send a horizontally
        scrollable carousel of items, each composed of an image, text and buttons.

        **Reference**: https://developers.facebook.com/docs/messenger-platform/reference/template/generic/

        :type elements: list
        :param elements: An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.
        :type shareable: bool
        :param sharable: *Optional*. Set to true to enable the native share button in Messenger for the template message. Defaults to false. Shareable icon wont come if there are more than one elements.
        :type image_aspect_ratio: str
        :param image_aspect_ratio: *Optional*. The aspect ratio used to render images specified by element.image_url. Must be horizontal (1.91:1) or square (1:1). Defaults to horizontal.

        :returns: creates and returns a generic payload
        """
        message = self.__generate_generic_payload(
            elements, shareable, image_aspect_ratio)
        if message is None:
            return None
        else:
            generic_payload = self.utility.create_basic_recipient(self.user_id)
            generic_payload[self.tags.TAG_MESSAGE] = message
            return generic_payload

    def __generate_generic_payload(self, elements: list, shareable: bool = False, image_aspect_ratio: str = "horizontal"):
        """
        The generic template allows you to send a structured message that includes an image, text and buttons.
        A generic template with multiple templates described in the elements array will send a horizontally
        scrollable carousel of items, each composed of an image, text and buttons.

        **Reference**: https://developers.facebook.com/docs/messenger-platform/reference/template/generic/

        :type elements: list
        :param elements: An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.
        :type shareable: bool
        :param sharable: *Optional*. Set to true to enable the native share button in Messenger for the template message. Defaults to false. Shareable icon wont come if there are more than one elements.
        :type image_aspect_ratio: str
        :param image_aspect_ratio: *Optional*. The aspect ratio used to render images specified by element.image_url. Must be horizontal (1.91:1) or square (1:1). Defaults to horizontal.

        :returns: Generate each payload for Generic Template
        """
        if elements is None or len(elements) == 0:
            # Error
            logging.error("generic_template - elements are None or empty list")
            return None
        if len(elements) > 10:
            # Error
            logging.error(
                "generic_template - There are more than 10 elements on the list")
            return None

        if image_aspect_ratio not in (self.tags.TAG_IMAGE_ASPECT_RATIO_SQ, self.tags.TAG_IMAGE_ASPECT_RATIO_HR):
            # Error
            logging.error(
                "generic_template - image aspect ratio did not match the criteria")
            return None

        if type(shareable) != bool:
            logging.error("generic_template - shareable is not a boolean")
            return None

        # Check & Validate every single elements object
        for element in elements:
            if not self.validate_generic_element(element):
                # Error - Not validated
                logging.error("generic_template - validation error of an element")
                return None

        payload = {
            self.tags.TAG_TEMPLATE_TYPE: self.tags.TAG_TEMPLATE_TYPE_GENERIC,
            self.tags.TAG_SHAREABLE: shareable,
            self.tags.TAG_IMAGE_ASPECT_RATIO: image_aspect_ratio,
            self.tags.TAG_ELEMENTS: elements
        }
        return {
            self.tags.TAG_ATTACHMENT: {
                self.tags.TAG_TYPE: self.tags.TAG_TEMPLATE,
                self.tags.TAG_PAYLOAD: payload
            }
        }

    def validate_generic_element(self, element: dict):
        """
        Validate the generic elements object against the requirements mentioned on facebook doc.

        :param element: dict
        :param element: Element has to be a dictionary (To be validated properly!)

        :returns: bool success is True: DUH!
        """
        if element is None:
            logging.error("validate_generic_element - No element")
            return False
        title = element[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in element else None
        subtitle = element[self.tags.TAG_SUBTITLE] if self.tags.TAG_SUBTITLE in element else None
        image_url = element[self.tags.TAG_IMAGE_URL] if self.tags.TAG_IMAGE_URL in element else None
        default_action = element[self.tags.TAG_DEFAULT_ACTION] if self.tags.TAG_DEFAULT_ACTION in element else None
        buttons = element[self.tags.TAG_BUTTONS] if self.tags.TAG_BUTTONS in element else None

        if title is None or len(title) == 0:
            # Error
            logging.error(
                "validate_generic_element - title is None or empty string")
            return False
        if len(title) > 80:
            # Not Error. Bt Extra chars will be trimmed off
            logging.warn(
                "validate_generic_element - title has more 80 characters.")
        if subtitle is not None:
            if len(subtitle) > 80:
                # Not Error. Bt Extra chars will be trimmed off
                logging.warn(
                    "validate_generic_element - subtitle has more than 80 characters")
        if image_url is not None:
            # Url validation
            if not (self.utility.url_validation(image_url)):
                # Error
                logging.error(
                    "validate_generic_element - image_url validation failed")
                return False

        if default_action is not None:
            # button validation
            if not self.btn_validation.button_validation(default_action, self.tags.TAG_WEB_URL):
                # Error - Validate against web_url only for default_action btn
                logging.error(
                    "validate_generic_element - default action button validation failed")
                return False
        if buttons is not None:
            # buttons validation
            if len(buttons) > 3:
                # Error
                logging.error(
                    "validate_generic_element - maximum 3 buttons are allowed")
                return False
            for btn in buttons:
                if not self.btn_validation.button_validation(btn):
                    # Error - validate against all button type
                    logging.error(
                        "validate_generic_element - button validation failed!")
                    return False
        return True

    def create_single_generic_elements(self, title: str, subtitle: str = None, image_url: str = None, default_action: dict = None, buttons: list = None):
        """
        An array of element objects that describe instances of the generic template to be sent.
        Specifying multiple elements will send a horizontally scrollable carousel of templates.
        A maximum of 10 elements is supported.

        *This function works for both Generic Element and as well as to create
        an element for share_contents*

        :type title: str
        :param title: The title to display in the template. 80 character limit.
        :type title: str
        :type subtitle: *Optional*. The subtitle to display in the template. 80 character limit.
        :type image_url: str
        :param image_url: *Optional*. The URL of the image to display in the template.
        :type default_action: dict
        :param default_action: *Optional*. The default action executed when the template is tapped. Accepts the same properties as URL button, except title.
        :type buttons: list
        :param buttons: *Optional*. An array of buttons to append to the template. A maximum of 3 buttons per element is supported.

        :returns: Returns a single generic template element.
        """
        payload = {
            self.tags.TAG_TITLE: title,
            self.tags.TAG_SUBTITLE: subtitle,
            self.tags.TAG_IMAGE_URL: image_url,
            self.tags.TAG_DEFAULT_ACTION: default_action,
            self.tags.TAG_BUTTONS: buttons
        }
        if self.validate_generic_element(payload):
            # All validation filtered through. OoooooOOooooooO
            return payload
        else:
            return None
