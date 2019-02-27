from bizarro.utility.mother import MotherClass
from bizarro.buttons.button_validator import ButtonValidation


class GenericTemplate(MotherClass):

    def __init__(self, facebook_user_id):
        super().__init__()
        self.user_id = facebook_user_id
        self.btn_validation = ButtonValidation()

    def generic_template(self, elements: list, shareable: bool = False, image_aspect_ratio: str = "horizontal"):
        """
        https://developers.facebook.com/docs/messenger-platform/reference/template/generic/
        The generic template allows you to send a structured message that includes an image, text and buttons.
        A generic template with multiple templates described in the elements array will send a horizontally
        scrollable carousel of items, each composed of an image, text and buttons.
        :elements: list An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.
        :sharable: bool Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false. Shareable icon wont come if there are more than one elements.
        :image_aspect_ratio: str Optional. The aspect ratio used to render images specified by element.image_url. Must be horizontal (1.91:1) or square (1:1). Defaults to horizontal.
        """
        message = self.generate_generic_payload(
            elements, shareable, image_aspect_ratio)
        if message is None:
            # cause validatio in another function.
            return None
        else:
            generic_payload = self.utility.create_basic_recipient(self.user_id)
            generic_payload[self.tags.TAG_MESSAGE] = message
            return generic_payload

    def generate_generic_payload(self, elements: list, shareable: bool = False, image_aspect_ratio: str = "horizontal"):
        """
        https://developers.facebook.com/docs/messenger-platform/reference/template/generic/
        The generic template allows you to send a structured message that includes an image, text and buttons.
        A generic template with multiple templates described in the elements array will send a horizontally
        scrollable carousel of items, each composed of an image, text and buttons.
        :elements: list An array of element objects that describe instances of the generic template to be sent. Specifying multiple elements will send a horizontally scrollable carousel of templates. A maximum of 10 elements is supported.
        :sharable: bool Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false. Shareable icon wont come if there are more than one elements.
        :image_aspect_ratio: str Optional. The aspect ratio used to render images specified by element.image_url. Must be horizontal (1.91:1) or square (1:1). Defaults to horizontal.
        """
        if elements is None or len(elements) == 0:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_template", "elements cannot be None or an empty list. Elements: {}".format(
                elements), self.zathura_utility.Tag_Log_ERROR)
            return None
        if len(elements) > 10:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_template", "Maximum 10 elements are allowed. Elements: {}".format(
                len(elements)), self.zathura_utility.Tag_Log_ERROR)
            return None

        if image_aspect_ratio not in (self.tags.TAG_IMAGE_ASPECT_RATIO_SQ, self.tags.TAG_IMAGE_ASPECT_RATIO_HR):
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_template", "Image aspect ratio can either be horizontal or square. Image Aspect Ratio: {}".format(
                image_aspect_ratio), self.zathura_utility.Tag_Log_ERROR)
            return None

        if type(shareable) != bool:
            self.zathura.insert_error_log(self.user_id, "generic_template", "Shareable can either be True or False. shareable: {}".format(
                shareable), self.zathura_utility.Tag_Log_ERROR)
            return None

        # Check & Validate every single elements object
        for element in elements:
            if not self.validate_generic_element(element):
                # Error - Not validated
                self.zathura.insert_error_log(
                    self.user_id, "generic_template", "Element did not pass validation", self.zathura_utility.Tag_Log_ERROR)
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
        :element: dict has to be a fucking dictionary !!.
        :returns :bool success is True: DUH!
        """
        if element is None:
            return False
        title = element[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in element else None
        subtitle = element[self.tags.TAG_SUBTITLE] if self.tags.TAG_SUBTITLE in element else None
        image_url = element[self.tags.TAG_IMAGE_URL] if self.tags.TAG_IMAGE_URL in element else None
        default_action = element[self.tags.TAG_DEFAULT_ACTION] if self.tags.TAG_DEFAULT_ACTION in element else None
        buttons = element[self.tags.TAG_BUTTONS] if self.tags.TAG_BUTTONS in element else None
        error_name = "Validate Generic Element"
        if title is None or len(title) == 0:
            # Error
            self.zathura.insert_error_log(self.user_id, error_name, "Title cannot be None or empty length. Title: {}".format(
                title), self.zathura_utility.Tag_Log_ERROR)
            return False
        if len(title) > 80:
            # Not Error. Bt Extra chars will be trimmed off
            self.zathura.insert_error_log(self.user_id, error_name, "Title length is more than 80 chars limit. Title: {}".format(
                len(title)), self.zathura_utility.Tag_Log_INFO)
        if subtitle is not None:
            if len(subtitle) > 80:
                # Not Error. Bt Extra chars will be trimmed off
                self.zathura.insert_error_log(self.user_id, error_name, "Subtitle length is more than 80 chars limit. Subtitle: {}".format(
                    len(subtitle)), self.zathura_utility.Tag_Log_INFO)
        if image_url is not None:
            # Url validation
            if not (self.utility.url_validation(image_url)):
                # Error
                self.zathura.insert_error_log(self.user_id, error_name, "Image url is not valid. image_url: {}".format(
                    len(image_url)), self.zathura_utility.Tag_Log_WARNING)
                return False

        if image_url is None and subtitle is None:
            self.logger.info(
                "It would be better for the users if you add a subtitle or an image_url. It's better for the story you are trying to tell.")
        if default_action is not None:
            # button validation
            if not self.btn_validation.button_validation(default_action, self.tags.TAG_WEB_URL):
                # Error - Validate against web_url only for default_action btn
                self.zathura.insert_error_log(
                    self.user_id, error_name, "Default action button has not validate against web_url type", self.zathura_utility.Tag_Log_WARNING)
                return False
        if buttons is not None:
            # buttons validation
            if len(buttons) > 3:
                # Error
                self.zathura.insert_error_log(self.user_id, error_name, "At max 3 buttons is allowed for generic template. Current Buttons: {}".format(
                    len(buttons)), self.zathura_utility.Tag_Log_ERROR)
                return False
            for btn in buttons:
                if not self.btn_validation.button_validation(btn):
                    # Error - validate against all button type
                    self.zathura.insert_error_log(
                        self.user_id, error_name, "Buttons of generic type has not passed validation", self.zathura_utility.Tag_Log_ERROR)
                    return False
        if default_action is None and buttons is None:
            # Error
            self.logger.info(
                "You can create a generic element without any default action or buttons. However, wouldn't it be wiser if user actually able to click and do something with that card?")
        return True

    def create_single_generic_elements(self, title: str, subtitle: str = None, image_url: str = None, default_action: dict = None, buttons: list = None):
        """
        An array of element objects that describe instances of the generic template to be sent.
        Specifying multiple elements will send a horizontally scrollable carousel of templates.
        A maximum of 10 elements is supported.

        This function works for both Generic Element and as well as to create
        an element for share_contents

        :title :str The title to display in the template. 80 character limit.
        :subtitle :str Optional. The subtitle to display in the template. 80 character limit.
        :image_url :str Optional. The URL of the image to display in the template.
        :default_action :dict Optional. The default action executed when the template is tapped. Accepts the same properties as URL button, except title.
        :buttons :list Optional. An array of buttons to append to the template. A maximum of 3 buttons per element is supported.
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
