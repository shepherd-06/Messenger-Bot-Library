from bizarro.utility.mother import MotherClass


class ButtonValidation(MotherClass):

    def __init__(self):
        super().__init__()

    def button_validation(self, buttons: dict, button_type: str = None):
        """
        validates button againsts all button type.
        :buttons :dict button object that needs to be validate.
        :button_type :str if default_action button type needs to be validated.
        """
        if type(buttons) != dict:
            return False

        if self.tags.TAG_TYPE not in buttons:
            return False

        for key in buttons:
            if key == self.tags.TAG_TYPE:
                if (buttons[key] == self.tags.TAG_WEB_URL):
                    if button_type is not None:
                        return True if self.validate_web_url(buttons, True) else False
                    else:
                        return True if self.validate_web_url(buttons) else False
                elif (buttons[key] == self.tags.TAG_POSTBACK):
                    return True if self.validate_postback_button(buttons) else False
                elif buttons[key] == self.tags.TAG_PHONE_NUMEBR:
                    return True if self.validate_call_button(buttons) else False
        return True

    def validate_call_button(self, button: dict):
        """
        This functions validates button type: phone_number
        :button :dict Button element that needs to be varified as call button
        :returns :bool
        """
        btn_type = button[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in button else None 
        title = button[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in button else None
        phone_number = button[self.tags.TAG_PAYLOAD] if self.tags.TAG_PAYLOAD in button else None

        if btn_type is None or len(btn_type) == 0 or btn_type != self.tags.TAG_PHONE_NUMEBR:
            return False
        
        if title is None or len(title) == 0:
            return False
        
        if phone_number is not None or len(phone_number) > 0:
            import phonenumbers
            try:
                __phone_number = phonenumbers.parse(phone_number, None)
            except phonenumbers.phonenumberutil.NumberParseException:
                return False
            
            if not phonenumbers.is_valid_number(__phone_number):
                return False
        else:
            return False
        return True

    def validate_postback_button(self, button:dict):
        """
        This functions validates button type: postback 
        :button :dict Button element that needs to be varified as postback button
        :returns :bool
        """
        btn_type = button[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in button else None 
        title = button[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in button else None
        payload = button[self.tags.TAG_PAYLOAD] if self.tags.TAG_PAYLOAD in button else None

        if btn_type is None or len(btn_type) == 0:
            return False
        
        if btn_type != self.tags.TAG_POSTBACK:
            return False
        
        if title is None or len(title) == 0:
            return False

        if payload is None or len(payload) == 0 or len(payload) > 1000:
            return False
        return True


    def validate_web_url(self, button: dict, is_default_action: bool = False):
        """
        Validates button type web_url
        :button :dict Button element that needs to be varified as web_url
        :returns :bool
        """
        btn_type = button[self.tags.TAG_TYPE] if self.tags.TAG_TYPE in button else None
        url = button[self.tags.TAG_URL] if self.tags.TAG_URL in button else None
        title = button[self.tags.TAG_TITLE] if self.tags.TAG_TITLE in button else None
        webview_height_ratio = button[self.tags.TAG_WEBVIEW_HEIGHT_RATIO] if self.tags.TAG_WEBVIEW_HEIGHT_RATIO in button else None
        messenger_extension = button[self.tags.TAG_MESSENGER_EXTENSION] if self.tags.TAG_MESSENGER_EXTENSION in button else None
        fallback_url = button[self.tags.TAG_FALLBACK_URL] if self.tags.TAG_FALLBACK_URL in button else None

        if btn_type is None or btn_type != self.tags.TAG_WEB_URL:
            return False

        if url is None or len(url) == 0:
            return False

        if not self.utility.url_validation(url):
            return False
        
        if not is_default_action:
            if title is None or len(title) == 0:
                return False

        if type(messenger_extension) == bool:
            if messenger_extension:
                if fallback_url is None or len(fallback_url) == 0:
                    return False
                if not self.utility.https_url_validation(fallback_url):
                    return False

        if webview_height_ratio is not None:
            if webview_height_ratio not in (self.tags.TAG_ELEMENT_COMPACT, self.tags.TAG_WEBVIEW_HEIGHT_RATIO_FULL, self.tags.TAG_WEBVIEW_HEIGHT_RATIO_TALL):
                return False
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
