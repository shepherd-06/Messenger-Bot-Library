class QuickReply():
    reference = "https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies/"
    def __init__(self, user_id: str):
        """
        user_id: current user_id of the particular user
        """
        self.user_id = user_id
    
    def quick_reply_text(self, title: str, payload: list):
        """
        attachment is not enabled at this moment
        title: str contains the title of the quick reply payload.
        payload: list payload generated from quick_reply_payload_generator function.
        returns _quick_reply_complete_payload
        """
        pass

    def quick_reply_payload_generator(self, title_text: list, payload: list, image_url: list,  content_type: str = 'text'):
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
        returns quick_reply payloads
        """
        pass


if __name__ == '__main__':
    print("Quick Reply reference: {}".format(QuickReply('').reference))

#     {
#   "recipient":{
#     "id":"<PSID>"
#   },
#   "message":{
#     "text": "Here is a quick reply!",
#     "quick_replies":[
#       {
#         "content_type":"text",
#         "title":"Search",
#         "payload":"<POSTBACK_PAYLOAD>",
#         "image_url":"http://example.com/img/red.png"
#       },
#       {
#         "content_type":"location"
#       }
#     ]
#   }
# }