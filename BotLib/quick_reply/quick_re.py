from ZathuraProject import Zathura
from BotLib.utility.tag import Tags
from BotLib.utility.util import Utility

class QuickReply():
    reference = "https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies/"

    def __init__(self, user_id: str):
        """
        user_id: current user_id of the particular user
        """
        self.user_id = user_id
        self.zathura = Zathura()

    def quick_reply_text(self, title: str, payload: list):
        """
        attachment is not enabled at this moment. This will generate a complete payload for the quick reply
        title: str contains the title of the quick reply payload.
        payload: list payload generated from quick_reply_payload_generator function.
        returns _quick_reply_complete_payload
        """
        pass

    def quick_reply_payload_generator(self, title_text: list, payload: list, image_url: list,
                                      content_type: str = 'text'):
        """
        content_type is text here by default. if content_type is text, then all field is required, otherwise they are not required.
        content_type: text, location, user_phone_number, user_email
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
        Also, all of those list must be same size as well.
        returns quick_reply payloads
        """
        if content_type == 'text':
            quick_reply_payload = list()  # this is return payload
            if len(title_text) != len(payload) and len(payload) != len(image_url):
                self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'lists length did not match with each other', self.quick_reply_payload_generator.__name__)
                return list()
            for index in range(0, len(title_text)):
                _title = title_text[index]
                _payload = payload[index]
                _image_url = payload[index]
                if len(_payload) > 1000:
                    # error - length of payload cannot exceed 1000 characters limit
                    self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'payload length is more 1000 chars', self.quick_reply_payload_generator.__name__)
                    return list()
                if len(_title) > 20:
                    # generate soft warning message. 
                    self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'title length is more 20 characters limit. Excess chars will be truncated!', self.quick_reply_payload_generator.__name__)
                    continue  # this is a warning
                if _title == '' and _image_url == '':
                    # generate error. both cannot be empty
                    self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'title and image_url both cannot be empty for the same object', self.quick_reply_payload_generator.__name__)
                    return list()
                if _payload == '' and _image_url == '':
                    # generate error, both cannot be empty
                    self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'payload and image_url both cannot be empty for the same object', self.quick_reply_payload_generator.__name__)
                    return list()
                if len(_image_url) != 0:
                    # if there is any value in image_url then it would be checked
                    if not Utility.url_validation(_image_url):
                        self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'image url is not valid.', self.quick_reply_payload_generator.__name__)
                        return list()
                # All validation passed at this point.
                quick_reply_payload.append({
                    Tags.TAG_CONTENT_TYPE_TEXT: content_type,
                    Tags.TAG_TITLE: _title,
                    Tags.TAG_PAYLOAD: _payload,
                    Tags.TAG_IMAGE_URL: _image_url,
                })         
        else:
            quick_reply_payload = list()  # this is return payload
            if len(title_text) != len(payload) and len(payload) != len(image_url):
                self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'lists length did not match with each other', self.quick_reply_payload_generator.__name__)
                return list()
            for index in range(0, len(title_text)):
                _title = title_text[index]
                _payload = payload[index]
                _image_url = payload[index]
                # no validation required for other type of content type since none of them are required anyway
                if len(_image_url) != 0:
                    # if there is any value in image_url then it would be checked
                    if not Utility.url_validation(_image_url):
                        self.zathura.insert_error_log(self.user_id, 'quick_reply_payload', 'image url is not valid.', self.quick_reply_payload_generator.__name__)
                        return list()
                # if image_url is not valid, fb won't let you to post it anyway! better have no image_url for content type other than text
                # All validation passed at this point.
                quick_reply_payload.append({
                    Tags.TAG_CONTENT_TYPE_TEXT: content_type,
                    Tags.TAG_TITLE: _title,  # not necessary
                    Tags.TAG_PAYLOAD: _payload,  # not necessary
                    Tags.TAG_IMAGE_URL: _image_url,  # not necessary
                })
        return quick_reply_payload


def __quick_reply_payload_validation(self, payload: list):
    """
    this function validate the quick reply payload before sending it back to 
    calling function.
    """
    for items in payload:
        if Tags.TAG_CONTENT_TYPE_TEXT in items:
            _content_type = items[Tags.TAG_CONTENT_TYPE_TEXT]
            if _content_type == 'text':
                _title = items[Tags.TAG_TITLE] if Tags.TAG_TITLE in items else None
                _payload = items[Tags.TAG_PAYLOAD] if Tags.TAG_PAYLOAD in items else None
                _image_url = items[Tags.TAG_IMAGE_URL] if Tags.TAG_IMAGE_URL in items else None

                # check here title, payload and image_url
                if _image_url is not None:
                    if not Utility.url_validation(_image_url):
                        # url is not valid.
                        pass
            else:
                if Tags.TAG_IMAGE_URL in items:
                    _image_url = items[Tags.TAG_IMAGE_URL]
                    if not Utility.url_validation(_image_url):
                        # url is not valid.
                        pass


if __name__ == '__main__':
    print("Quick Reply reference: {}".format(QuickReply('').reference))
