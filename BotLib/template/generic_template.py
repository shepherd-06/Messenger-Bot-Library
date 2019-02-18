from BotLib.utility.mother import MotherClass
from BotLib.utility.button_validation import ButtonValidation


class GenericTemplate(MotherClass):

    def __init__(self, facebook_user_id):
        super().__init__()
        self.user_id = facebook_user_id
        self.btn_validation = ButtonValidation()

    def create_single_generic_elements(self, title: str, subtitle: str = None, image_url: str = None, default_action: dict = None, buttons: list = None):
        """
        An array of element objects that describe instances of the generic template to be sent.
        Specifying multiple elements will send a horizontally scrollable carousel of templates.
        A maximum of 10 elements is supported.
        :title :str The title to display in the template. 80 character limit.
        :subtitle :str Optional. The subtitle to display in the template. 80 character limit.
        :image_url :str Optional. The URL of the image to display in the template.
        :default_action :dict Optional. The default action executed when the template is tapped. Accepts the same properties as URL button, except title.
        :buttons :list Optional. An array of buttons to append to the template. A maximum of 3 buttons per element is supported.
        """
        if title is None or len(title) == 0:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_elements_create", "Title cannot be None or empty length. Title: {}".format(
                title), self.zathura_utility.Tag_Log_ERROR)
            return
        if len(title) > 80:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_elements_create", "Title length is more than 80 chars limit. Title: {}".format(
                len(title)), self.zathura_utility.Tag_Log_WARNING)
            pass
        if len(subtitle) > 80:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_elements_create", "Subtitle length is more than 80 chars limit. Subtitle: {}".format(
                len(subtitle)), self.zathura_utility.Tag_Log_WARNING)
            pass
        if image_url is not None:
            # Url validation
            if not (self.utility.url_validation(image_url)):
                # Error
                pass
        if default_action is not None:
            # button validation
            if not self.btn_validation.button_validation(default_action, self.tags.TAG_WEB_URL):
                # Error - Validate against web_url only for default_action btn
                pass
        if buttons is not None:
            # buttons validation
            if len(buttons) > 3:
                # Error
                self.zathura.insert_error_log(self.user_id, "generic_elements_create", "At max 3 buttons is allowed for generic template. Current Buttons: {}".format(len(buttons)), self.zathura_utility.Tag_Log_ERROR)
                return
            for btn in buttons:
                if not self.btn_validation.button_validation(btn):
                    # Error - validate against all button type
                    pass
        if default_action is None and buttons is None:
            # Error
            self.zathura.insert_error_log(self.user_id, "generic_elements_create", "Both default actions and buttons cannot be None. At least one button element or default action must be mentioned.", self.zathura_utility.Tag_Log_ERROR)
            return
        
        # All validation filtered through. OoooooOOooooooO
        return {
            self.tags.TAG_TITLE: title,
            self.tags.TAG_SUBTITLE: subtitle,
            self.tags.TAG_IMAGE_URL: image_url,
            self.tags.TAG_DEFAULT_ACTION: default_action,
            self.tags.TAG_BUTTONS: buttons
        }