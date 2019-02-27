from bizarro.utility.tag import Tags
from bizarro.utility.util import Utility
from ZathuraProject.zathura import Zathura
from ZathuraProject.utility import Utility as ZathuraUtility


class QuickReply():
    reference = "https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies/"

    def __init__(self, user_id: str):
        """
        user_id: current user_id of the particular user
        """
        self.user_id = user_id
        self.utility = Utility()
        self.zathura = Zathura()
        self.zathura_utility = ZathuraUtility()

    def quick_reply(self, title: str, payload: list):
        """
        attachment is not enabled at this moment. This will generate a complete payload for the quick reply
        title: str contains the title of the quick reply payload.
        payload: list payload generated from quick_reply_payload_generator function.
        returns _quick_reply_complete_payload
        """
        zathura_error_name = "quick_reply"
        if type(payload) != list:
            self.zathura.insert_error_log(
                self.user_id, zathura_error_name, "payload should be a list not a {}".format(type(payload)), self.zathura_utility.Tag_Log_ERROR)
            return
        if not self.__quick_reply_payload_validation(payload):
            self.zathura.insert_error_log(
                self.user_id, zathura_error_name, "quick reply payload invalid", self.zathura_utility.Tag_Log_ERROR)
            return

        if title is None or len(title) == 0:
            self.zathura.insert_error_log(
                self.user_id, zathura_error_name, "quick reply title cannot be None or empty string", self.zathura_utility.Tag_Log_ERROR)
            return
        message = {
            Tags.TAG_TEXT: title,
            Tags.TAG_QUICK_REPLIES: payload,
        }
        quick_reply_payload = self.utility.create_basic_recipient(
            self.user_id)
        quick_reply_payload[Tags.TAG_MESSAGE] = message
        self.zathura.insert_debug_log(quick_reply_payload)
        return quick_reply_payload

    def __quick_reply_payload_validation(self, payload: list):
        """
        this function validate the quick reply payload before sending it back to 
        calling function.
        """
        error_name = "q_reply_payload_validation"
        if len(payload) > 11:
            # error - payload cannot have more than 11 items
            self.zathura.insert_error_log(
                self.user_id, error_name, '"A maximum of 11 quick replies are supported"', self.zathura_utility.Tag_Log_ERROR)
            return False
        for items in payload:
            if Tags.TAG_CONTENT_TYPE in items:
                _content_type = items[Tags.TAG_CONTENT_TYPE]
                if _content_type == 'text':
                    _title = items[Tags.TAG_TITLE] if Tags.TAG_TITLE in items else None
                    _payload = items[Tags.TAG_PAYLOAD] if Tags.TAG_PAYLOAD in items else None
                    _image_url = items[Tags.TAG_IMAGE_URL] if Tags.TAG_IMAGE_URL in items else None

                    # check here title, payload and image_url
                    if _image_url is not None:
                        if len(_image_url) > 0:
                            if not Utility.url_validation(_image_url):
                                # url is not valid
                                self.zathura.insert_error_log(
                                    self.user_id, error_name, 'image_url invalid', self.zathura_utility.Tag_Log_ERROR)
                                return False
                    if _title is None and _image_url is None:
                        # error:
                        self.zathura.insert_error_log(
                            self.user_id, error_name, 'title and image_url both are none', self.zathura_utility.Tag_Log_ERROR)
                        return False
                    if _image_url is None and _payload is None:
                        # error
                        self.zathura.insert_error_log(
                            self.user_id, error_name, 'payload and image_url both are none', self.zathura_utility.Tag_Log_ERROR)
                        return False
                else:
                    if Tags.TAG_IMAGE_URL in items:
                        _image_url = items[Tags.TAG_IMAGE_URL]
                        if len(_image_url) > 0:
                            if not Utility.url_validation(_image_url):
                                # url is not valid.
                                self.zathura.insert_error_log(
                                    self.user_id, error_name, 'url is not valid', self.zathura_utility.Tag_Log_ERROR)
                                return False
            else:
                return False
        return True

    def quick_reply_create(self, content_type: str, title_text: str = '', payload: str = '', image_url: str = ''):
        """
        generates a single entry payload for quick reply. It makes it easier to generate 
        payload for quick reply
        content_type: str text, location, user_phone_number, user_email
        title_text: 1) contains titles of each field. maximum of 11 quick replies are supported.
                    2) Required if content_type is 'text'. 
                    3) The text to display on the quick reply button.
                    4) 20 characters limit.
        payload: 1) Required if content_type is 'text'. 
                 2) Custom data that will be sent back to you via the messaging_postbacks webhook event.
                 3) 1000 characters limit.
                 4) May be set to an empty string if image_url is set.
        image_url: 1) Optional. URL of image to display on the quick reply button for text quick replies.
                   2) Image should be a minimum of 24px x 24px. Larger images will be automatically cropped and resized.
                   3) Required if title is an empty string.
        title_text, payload and image_url must have non zero list, if required set the value of every index to empty string to avoid confusion.
        """
        error_name = 'quick_reply_create'
        if content_type == Tags.TAG_CONTENT_TYPE_TEXT:
            if len(payload) > 1000:
                # error - length of payload cannot exceed 1000 characters limit
                self.zathura.insert_error_log(
                    self.user_id, error_name, 'payload length is more 1000 chars', self.zathura_utility.Tag_Log_ERROR)
                return {}
            if len(title_text) > 20:
                # generate soft warning message.
                self.zathura.insert_error_log(
                    self.user_id, error_name, 'title length is more 20 characters limit. Excess chars will be truncated!', self.zathura_utility.Tag_Log_WARNING)
                pass  # this is a warning
            if title_text == '' and image_url == '':
                # generate error. both cannot be empty
                self.zathura.insert_error_log(
                    self.user_id, error_name, 'title and image_url both cannot be empty for the same object', self.zathura_utility.Tag_Log_ERROR)
                return {}
            if payload == '' and image_url == '':
                # generate error, both cannot be empty
                self.zathura.insert_error_log(
                    self.user_id, error_name, 'payload and image_url both cannot be empty for the same object', self.zathura_utility.Tag_Log_ERROR)
                return {}
            if len(image_url) != 0:
                # if there is any value in image_url then it would be checked
                if not Utility.url_validation(image_url):
                    self.zathura.insert_error_log(
                        self.user_id, error_name, 'image url is not valid.', self.zathura_utility.Tag_Log_ERROR)
                    return {}
        return {
            Tags.TAG_CONTENT_TYPE: content_type,
            Tags.TAG_TITLE: title_text,
            Tags.TAG_PAYLOAD: payload,
            Tags.TAG_IMAGE_URL: image_url,
        }
