from bizarro_lib.utility.mother import MotherClass


class ButtonValidation(MotherClass):

    def __init__(self):
        super().__init__()

    def button_validation(self, buttons: dict, button_type: str = None):
        """
        """
        return True

    def validate_generic_share_elements(self, share_contents: dict):
        """
        Optional. The message that you wish the recipient of the share to see, 
        if it is different from the one this button is attached to. 
        The format follows that used in Send API.
        share_contents only supports the following:
         - Template used must be generic template.
         - Maximum of one URL button on the template. If no buttons are specified, 
           the buttons property on the generic template must be set to an empty array.
        """
        if share_contents is not None:
            if self.tags.TAG_ATTACHMENT in share_contents:
                attachments = share_contents[self.tags.TAG_ATTACHMENT]
                if not self.tags.TAG_TYPE in attachments:
                    # Error - TODO
                    return False
                if self.tags.TAG_ELEMENTS in attachments:
                    elements = attachments[self.tags.TAG_ELEMENTS]
                    for element in elements:
                        if not self.tags.TAG_TITLE in element:
                            pass
                        if not self.tags.TAG_SUBTITLE in element:
                            pass
                        if not self.tags.TAG_IMAGE_URL in element:
                            pass
                        if self.tags.TAG_DEFAULT_ACTION in element:
                            default_action = element[self.tags.TAG_DEFAULT_ACTION]
                            if self.tags.TAG_TYPE in default_action:
                                def_type = default_action[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in default_action else None
                                def_url = default_action[self.tags.TAG_URL] if self.tags.TAG_URL in default_action else None

                                if def_type != self.tags.TAG_WEB_URL:
                                    # Error - TODO
                                    return False

                                if def_url is not None:
                                    if not self.utility.url_validation(def_url):
                                        # Error - TODO
                                        return False                                
                        else:
                            # Does not matter 
                            pass
                        if self.tags.TAG_BUTTONS in element:
                            buttons = element[self.tags.TAG_BUTTONS]
                            if type(buttons) != type(list):
                                # Error - TODO
                                return False
                            if len(buttons) > 1:
                                # Error - TODO
                                return False
                            if len(buttons) == 1:
                                button = buttons[0]
                                btn_type = button[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in button else None
                                btn_url = button[self.tags.TAG_URL] if self.tags.TAG_URL in button else None
                                btn_title = button[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in button else None

                                if btn_type != self.tags.TAG_WEB_URL:
                                    # Error - TODO
                                    return False
                                if btn_url is None:
                                    # Error - TODO
                                    return False
                                else:
                                    if not self.utility.url_validation(btn_url):
                                        # Error - TODO
                                        return False
                                if btn_title is None or len(btn_title) == 0:
                                    # Error - TODO (may be)
                                    pass
                        else:
                            # Error
                            return False
                else:
                    # Error - TODO
                    return False
            else:
                # Error - TODO
                return False
        # If share_content is not None, then everything must be checked 
        # cause fb will try to parse through everything.
        return True