from bizarro.buttons.button_validator import ButtonValidation
from bizarro.utility.mother import MotherClass


class ButtonTemplate(MotherClass):
    def __init__(self, facebook_user_id):
        super().__init__()
        self.user_id = facebook_user_id
        self.button_validate = ButtonValidation()

    def button_template(self, title_text: str, buttons: list, sharable: bool = False):
        """
        Creates a template format for button template
        reference: https://developers.facebook.com/docs/messenger-platform/reference/template/button/
        :title_text :str UTF-8-encoded text of up to 640 characters. Text will appear above the buttons.
        :buttons :list Set of 1-3 buttons that appear as call-to-actions.
        :shareable :bool Optional. Set to true to enable the native share button in Messenger for the template message. Defaults to false.
        :return Button_Template in the form of a dictionary
        """
        if title_text is None or len(title_text) == 0:
            # Error
            self.zathura.insert_error_log(
                self.user_id, "title", "title is either None or len = 0. Title {}".format(title_text), self.zathura_utility.Tag_Log_ERROR)
            return

        if len(title_text) > 640:
            # Probably Warning
            self.zathura.insert_error_log(self.user_id, "title", "Length of title text is more 640 chars. Title {}".format(
                len(title_text)), self.zathura_utility.Tag_Log_ERROR)
            return

        if buttons is None or len(buttons) == 0:
            # Error
            self.zathura.insert_error_log(
                self.user_id, "buttons", "buttons is either None or len = 0. Title {}".format(buttons), self.zathura_utility.Tag_Log_ERROR)
            return

        if len(buttons) > 3:
            # Error
            self.zathura.insert_error_log(self.user_id, "buttons", "There must be AT MAX 3 buttons. Buttons: {}".format(
                len(buttons)), self.zathura_utility.Tag_Log_WARNING)
            return
        for button in buttons:
            if not self.button_validate.button_validation(button):
                # Error
                self.zathura.insert_error_log(
                    self.user_id, "buttons", "Buttons did not validate the correct format", self.zathura_utility.Tag_Log_ERROR)
                return

        # Now create payload
        payload = {
            self.tags.TAG_TEMPLATE_TYPE: self.tags.TAG_BUTTON,
            self.tags.TAG_TEXT: title_text,
            self.tags.TAG_BUTTONS: buttons
        }

        message = {
            self.tags.TAG_ATTACHMENT: {
                self.tags.TAG_TYPE: self.tags.TAG_TEMPLATE,
                self.tags.TAG_PAYLOAD: payload,
            }
        }

        button_template_payload = self.utility.create_basic_recipient(
            self.user_id)
        button_template_payload[self.tags.TAG_MESSAGE] = message
        return button_template_payload
