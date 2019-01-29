from BotLib.utility.tag import Tags

class Utility:

    @staticmethod
    def __create_basic_recipient(user_id: str):
        """
        :param user_id: facebook users user id.
        :return: creates the receipients payload
        """
        return {
            Tags.TAG_RECIPIENT: {
                Tags.TAG_ID: user_id
            }
        }

    def __typing_on(self, user_id: str, waiting_period:float =1.5):
        """
        private function, turns on typing function, sleep 3s before doing anything else.
        :param user_id:
        :return: returns the payload for typing_on function
        """
        payload = self.__create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_TYPING_ON
        return payload

    def marked_seen(self, user_id):
        """
        marked last message as seen in case there is no definitive action to be taken!
        :param user_id: facebook user id
        :return: payload to create a mark_seen on facebook messenger platform
        """
        payload = self.__create_basic_recipient(user_id)
        payload[Tags.TAG_SENDER_ACTION] = Tags.TAG_MARK_SEEN
        return payload

    def basic_text_reply_payload(self, user_id:str, message:str, typing_on:float = 1.5):
        """
        this functions generates the payload for basic text reply
        :param waiting_period: how long will the typing_on display run, default is 1.5 seconds
        :param user_id: user_id of a particular user_id
        :param message: message user going to see
        :return: payload
        """
        payload = {
                Tags.TAG_RECIPIENT: {
                    Tags.TAG_ID: user_id
                },
                Tags.TAG_MESSAGE: {
                    Tags.TAG_TEXT: message
                }
            }
        return payload    


# if __name__ == '__main__':
#     util = Utility()
#     x = util.basic_text_reply_payload('1234', 'dfsdf')
#     print(x)